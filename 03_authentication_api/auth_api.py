"""Authentication reference API.

Run locally:
  pip install -r requirements.txt
  uvicorn auth_api:app --reload

Use an external OIDC provider for production. Local JWT mode exists for development.
"""

import hashlib
import hmac
import os
from datetime import datetime, timedelta, timezone
from typing import Annotated, Any

import jwt
from fastapi import Depends, FastAPI, HTTPException, Security, status
from fastapi.security import (
    APIKeyHeader,
    HTTPBasic,
    HTTPBasicCredentials,
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)
from jwt import PyJWKClient
from pydantic import BaseModel, Field
from pwdlib import PasswordHash


class Settings:
    jwt_secret = os.getenv("JWT_SECRET", "replace-this-development-secret")
    jwt_algorithm = os.getenv("JWT_ALGORITHM", "HS256")
    jwt_issuer = os.getenv("JWT_ISSUER", "auth-api")
    jwt_audience = os.getenv("JWT_AUDIENCE", "auth-api-client")
    jwks_url = os.getenv("OIDC_JWKS_URL", "")
    oidc_issuer = os.getenv("OIDC_ISSUER", "")
    api_key = os.getenv("SERVICE_API_KEY", "local-service-key")
    basic_user = os.getenv("BASIC_AUTH_USER", "admin")
    basic_password_hash = os.getenv("BASIC_AUTH_PASSWORD_HASH", "")
    demo_user = os.getenv("DEMO_USER", "demo")
    demo_password_hash = os.getenv("DEMO_PASSWORD_HASH", "")
    access_token_minutes = int(os.getenv("ACCESS_TOKEN_MINUTES", "15"))


settings = Settings()
password_hash = PasswordHash.recommended()

app = FastAPI(title="Production Authentication API", version="1.0.0")
api_key_scheme = APIKeyHeader(name="X-API-Key", auto_error=False)
basic_scheme = HTTPBasic(auto_error=False)
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/token",
    scopes={"items:read": "Read items", "items:write": "Create or change items"},
)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int


class Principal(BaseModel):
    subject: str
    scopes: set[str] = Field(default_factory=set)
    auth_scheme: str


def unauthorized(detail: str = "Not authenticated") -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail,
        headers={"WWW-Authenticate": "Bearer"},
    )


def secret_matches(candidate: str, expected: str) -> bool:
    return bool(expected) and hmac.compare_digest(
        hashlib.sha256(candidate.encode()).digest(),
        hashlib.sha256(expected.encode()).digest(),
    )


def verify_password(password: str, stored_hash: str) -> bool:
    return bool(stored_hash) and password_hash.verify(password, stored_hash)


def create_local_token(subject: str, scopes: set[str]) -> str:
    now = datetime.now(timezone.utc)
    expires = now + timedelta(minutes=settings.access_token_minutes)
    return jwt.encode(
        {
            "sub": subject,
            "scope": " ".join(sorted(scopes)),
            "iss": settings.jwt_issuer,
            "aud": settings.jwt_audience,
            "iat": now,
            "exp": expires,
        },
        settings.jwt_secret,
        algorithm=settings.jwt_algorithm,
    )


def decode_token(token: str) -> dict[str, Any]:
    try:
        if settings.jwks_url:
            key = PyJWKClient(settings.jwks_url).get_signing_key_from_jwt(token).key
            return jwt.decode(
                token,
                key,
                algorithms=["RS256", "ES256"],
                issuer=settings.oidc_issuer,
                audience=settings.jwt_audience,
            )
        return jwt.decode(
            token,
            settings.jwt_secret,
            algorithms=[settings.jwt_algorithm],
            issuer=settings.jwt_issuer,
            audience=settings.jwt_audience,
        )
    except jwt.PyJWTError as exc:
        raise unauthorized("Invalid or expired token") from exc


async def require_api_key(api_key: Annotated[str | None, Security(api_key_scheme)]) -> Principal:
    if not api_key or not secret_matches(api_key, settings.api_key):
        raise unauthorized("Invalid API key")
    return Principal(subject="service", scopes={"items:read", "items:write"}, auth_scheme="api-key")


async def require_basic(
    credentials: Annotated[HTTPBasicCredentials | None, Depends(basic_scheme)],
) -> Principal:
    if not credentials or not settings.basic_password_hash:
        raise unauthorized("Basic authentication is not configured")
    valid_user = hmac.compare_digest(credentials.username, settings.basic_user)
    valid_password = verify_password(credentials.password, settings.basic_password_hash)
    if not (valid_user and valid_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return Principal(subject=credentials.username, scopes={"items:read"}, auth_scheme="basic")


async def require_bearer(
    security_scopes: SecurityScopes,
    token: Annotated[str, Depends(oauth2_scheme)],
) -> Principal:
    claims = decode_token(token)
    token_scopes = set(claims.get("scope", "").split())
    missing = set(security_scopes.scopes) - token_scopes
    if missing:
        raise HTTPException(status_code=403, detail=f"Missing scopes: {', '.join(sorted(missing))}")
    subject = claims.get("sub")
    if not subject:
        raise unauthorized("Token has no subject")
    return Principal(subject=subject, scopes=token_scopes, auth_scheme="oidc" if settings.jwks_url else "jwt")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok", "oidc": "enabled" if settings.jwks_url else "local-jwt"}


@app.post("/auth/token", response_model=Token)
async def issue_demo_token(form: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    if not verify_password(form.password, settings.demo_password_hash) or not hmac.compare_digest(
        form.username, settings.demo_user
    ):
        raise unauthorized("Invalid username or password")
    requested = set(form.scopes)
    allowed = {"items:read", "items:write"}
    if not requested.issubset(allowed):
        raise HTTPException(status_code=400, detail="Unsupported scope")
    return Token(
        access_token=create_local_token(form.username, requested),
        expires_in=settings.access_token_minutes * 60,
    )


@app.get("/v1/items/api-key")
async def api_key_example(_: Annotated[Principal, Depends(require_api_key)]) -> dict[str, str]:
    return {"message": "Authenticated with an API key"}


@app.get("/v1/items/basic")
async def basic_example(_: Annotated[Principal, Depends(require_basic)]) -> dict[str, str]:
    return {"message": "Authenticated with HTTP Basic"}


@app.get("/v1/items/bearer")
async def bearer_example(
    _: Annotated[Principal, Security(require_bearer, scopes=["items:read"])],
) -> dict[str, str]:
    return {"message": "Authenticated with a bearer token"}


@app.post("/v1/items/bearer")
async def bearer_write_example(
    _: Annotated[Principal, Security(require_bearer, scopes=["items:write"])],
) -> dict[str, str]:
    return {"message": "Authenticated with a bearer token and write scope"}
