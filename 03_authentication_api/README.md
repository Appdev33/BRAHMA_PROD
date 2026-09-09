# Authentication API

This API shows several ways to protect a FastAPI service. Authentication answers **“Who are you?”** Authorization answers **“What are you allowed to do?”**

The examples are intentionally in one small service so the differences are easy to compare. In a real product, choose the method based on the client and risk level. Do not enable every method for every endpoint without a reason.

## Start The API

Install dependencies:

```bash
cd 03_authentication_api
pip install -r requirements.txt
```

Start it:

```bash
uvicorn auth_api:app --reload --port 8001
```

Open the interactive documentation:

```text
http://127.0.0.1:8001/docs
```

## Endpoints

| Method | Endpoint | Protection |
|---|---|---|
| `GET` | `/health` | Public health check |
| `POST` | `/auth/token` | OAuth2 form login for local development |
| `GET` | `/v1/items/api-key` | API key |
| `GET` | `/v1/items/basic` | HTTP Basic |
| `GET` | `/v1/items/bearer` | Bearer token with `items:read` |
| `POST` | `/v1/items/bearer` | Bearer token with `items:write` |

## The Authentication Techniques

### 1. API key

**Simple idea:** A service receives a long secret in the `X-API-Key` header.

```bash
curl http://127.0.0.1:8001/v1/items/api-key \
  -H 'X-API-Key: local-service-key'
```

**Good for:** Internal services, scripts, scheduled jobs, and simple server-to-server calls.

**Advantages:**

- Very easy to implement.
- Easy for a machine to send.
- No login page or token service is required.
- Works well for low-complexity internal integrations.

**Tradeoffs:**

- Usually identifies an application, not a person.
- A stolen key works until it is revoked or rotated.
- Basic keys do not naturally contain user roles or fine-grained permissions.
- Key sharing makes auditing difficult.

**Code approach:** The API reads `X-API-Key` with `APIKeyHeader` and compares it using a constant-time comparison. The configured value should come from a secret manager.

**Production advice:** Use separate keys per client, expiration and rotation, IP or network restrictions, rate limits, and audit logs. Never put keys in source code or URLs.

### 2. HTTP Basic authentication

**Simple idea:** The client sends a username and password with every request.

```bash
curl -u admin:your-password http://127.0.0.1:8001/v1/items/basic
```

**Good for:** Small internal administration tools or temporary protected endpoints.

**Advantages:**

- Supported by almost every HTTP client.
- Very small implementation.
- Useful when there is no separate login system.

**Tradeoffs:**

- The password is sent on every request, encoded but not encrypted by Basic itself.
- HTTPS is mandatory.
- Password rotation and revocation are your responsibility.
- It is not a good fit for public mobile or browser applications.

**Code approach:** The API reads credentials with `HTTPBasic`, compares the username safely, and verifies an Argon2 password hash with `pwdlib`. It never needs to store the plaintext password.

**Production advice:** Use only behind HTTPS, keep it for narrow internal use, add rate limiting, and prefer an identity provider for normal users.

### 3. OAuth2 bearer token

**Simple idea:** The user or client authenticates once and receives a short-lived access token. Later requests send only that token.

```text
Authorization: Bearer <access-token>
```

The local demo endpoint is:

```bash
POST /auth/token
```

It accepts OAuth2 form fields: `username`, `password`, and optional `scope`.

**Good for:** APIs used by web applications, mobile applications, and first-party clients.

**Advantages:**

- Passwords are not sent to every business endpoint.
- Tokens can expire automatically.
- Works with scopes and delegated permissions.
- Supported by FastAPI's OpenAPI documentation.

**Tradeoffs:**

- A token is powerful if stolen before it expires.
- Token refresh, revocation, and storage need a complete design.
- The password-token endpoint is not a complete identity platform.
- OAuth2 terminology is easy to misconfigure.

**Code approach:** `OAuth2PasswordBearer` describes the bearer-token contract and points Swagger to `/auth/token`. `SecurityScopes` checks permissions such as `items:read` and `items:write`.

**Production advice:** Use an external identity provider. The local password flow in this example is for development or a tightly controlled first-party environment, not a general public login system.

### 4. JWT access tokens

**Simple idea:** A JWT is a signed JSON document containing claims such as the user ID, issuer, audience, scopes, issue time, and expiry time.

**Good for:** Stateless APIs where many API instances need to validate a token without calling a session database for every request.

**Advantages:**

- Fast local verification after the signing key is available.
- Works across many API replicas.
- Can carry scopes and identity claims.
- Expiry is built into the token.

**Tradeoffs:**

- JWT data is encoded, not secret. Do not put passwords or sensitive data in it.
- Revoking a token before expiry is harder than deleting a server session.
- Large tokens increase request size.
- Accepting the wrong algorithm, issuer, or audience creates a serious security issue.

**Code approach:** `decode_token()` verifies the signature, allowed algorithm, issuer, audience, and expiry. The API rejects tokens without a subject and checks required scopes.

**Production advice:** Use short access-token lifetimes, rotate signing keys, keep refresh tokens outside browser JavaScript where possible, and plan revocation for high-risk actions.

### 5. OIDC and JWKS validation

**Simple idea:** A specialist identity provider handles login, multifactor authentication, password recovery, social login, and key rotation. The API only verifies the provider's signed token.

Examples of providers include Auth0, Keycloak, Okta, Microsoft Entra ID, and Amazon Cognito.

Configure:

```bash
export OIDC_ISSUER='https://identity.example.com/'
export OIDC_JWKS_URL='https://identity.example.com/.well-known/jwks.json'
export JWT_AUDIENCE='items-api'
```

**Good for:** Production systems with real users, multiple applications, single sign-on, multifactor authentication, or enterprise identity requirements.

**Advantages:**

- The API does not manage user passwords.
- Centralized login and account lifecycle management.
- Supports multifactor authentication and enterprise SSO.
- Public signing keys can be rotated and discovered through JWKS.
- One identity can be used across multiple services.

**Tradeoffs:**

- Adds an external dependency and operational cost.
- Provider configuration must be correct.
- Provider outages can affect login and key discovery.
- User roles and scopes still need careful mapping inside the API.
- Vendor migration requires planning.

**Code approach:** When `OIDC_JWKS_URL` is configured, `PyJWKClient` obtains the provider's public signing key and the API validates the token using the configured issuer and audience. The API never receives the user's password.

**Production advice:** Cache JWKS keys with a refresh strategy, validate `iss`, `aud`, `exp`, and signature algorithm, monitor key rotation, use HTTPS, and test provider failure behavior.

## Authorization And Scopes

Authentication alone is not enough. A valid user should not automatically be allowed to perform every action.

This API demonstrates two scopes:

- `items:read`: may call the bearer-token read endpoint.
- `items:write`: may call the bearer-token write endpoint.

A token without the required scope receives `403 Forbidden`. A missing or invalid token receives `401 Unauthorized`.

## Configuration

| Variable | Purpose |
|---|---|
| `SERVICE_API_KEY` | Expected API key |
| `BASIC_AUTH_USER` | Basic-auth username |
| `BASIC_AUTH_PASSWORD_HASH` | Argon2 hash for the Basic password |
| `DEMO_USER` | Local OAuth2 demo username |
| `DEMO_PASSWORD_HASH` | Argon2 hash for the local OAuth2 demo password |
| `JWT_SECRET` | Local-development JWT signing secret |
| `JWT_ISSUER` | Expected local JWT issuer |
| `JWT_AUDIENCE` | Expected token audience |
| `OIDC_ISSUER` | External identity-provider issuer |
| `OIDC_JWKS_URL` | External provider public-key endpoint |

Create password hashes:

```bash
python -c 'from pwdlib import PasswordHash; print(PasswordHash.recommended().hash("change-me"))'
```

## Choosing The Right Scheme

| Situation | Recommended choice |
|---|---|
| Internal scheduled job | API key with rotation |
| Short-lived internal admin tool | Basic auth over HTTPS, or preferably SSO |
| Public web or mobile application | OIDC authorization code flow |
| Several backend services | OIDC/JWT or mTLS for service identity |
| High-risk financial or administrative action | OIDC plus MFA, scopes, and step-up verification |
| Need immediate session revocation | Server-side sessions or opaque tokens |

There is no single best scheme for every client. The safest default for a user-facing production system is an external OIDC provider with short-lived access tokens, scoped authorization, MFA where appropriate, rate limiting, audit logs, and a secrets manager.

## Production Checklist

- Use a real OIDC provider instead of the local demo password endpoint.
- Store all secrets in a secrets manager.
- Require HTTPS and reject insecure proxy configuration.
- Rotate API keys and signing keys.
- Use short-lived access tokens.
- Validate issuer, audience, expiry, subject, and algorithm.
- Add rate limits and account lockout protections.
- Log authentication events without logging passwords or tokens.
- Add tests for every failure case: missing, expired, altered, wrong-audience, and insufficient-scope tokens.
- Add a revocation strategy for logout, compromised credentials, and high-risk actions.
