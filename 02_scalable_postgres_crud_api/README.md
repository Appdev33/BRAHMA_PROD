# Scalable CRUD API

A separate FastAPI service designed as a production-oriented starting point for a high-traffic CRUD API.

## What This API Does

This service manages simple items. An item can be created, viewed, listed, edited, or deleted.

In simple terms:

- **FastAPI** receives web requests and returns JSON responses.
- **PostgreSQL** permanently stores the real data.
- **Redis** keeps popular data temporarily so repeated requests are fast.
- **Docker Compose** starts the API, database, and cache together.

The API can run as multiple identical copies behind a load balancer because it does not keep user data inside application memory.

## Run locally

From this directory:

```bash
docker compose up --build
```

Open `http://localhost:8000/docs` for Swagger UI.

The Swagger page lets you try every endpoint from a browser.

## Endpoints

- `GET /health`
- `POST /v1/items`
- `GET /v1/items?limit=20&offset=0`
- `GET /v1/items/{id}`
- `PUT /v1/items/{id}`
- `DELETE /v1/items/{id}`

Example create request:

```bash
curl -X POST http://localhost:8000/v1/items \
	-H 'Content-Type: application/json' \
	-d '{"name":"Revision note","description":"Important backend concept"}'
```

The response contains the generated item ID. Use that ID with the read, update, and delete endpoints.

## Features In Plain Language

| Feature | What it means |
|---|---|
| Create, read, update, delete | The complete basic data-management workflow |
| Input validation | Bad or oversized data is rejected before it reaches the database |
| PostgreSQL | Reliable shared storage suitable for multiple API instances |
| Async request handling | The server can handle other requests while waiting for the database |
| Connection pooling | Database connections are reused instead of recreated for every request |
| Redis caching | Frequently requested items can be returned faster |
| Cache fallback | The API still reads from PostgreSQL if Redis is unavailable |
| Negative caching | Repeated requests for missing IDs do not constantly hit PostgreSQL |
| TTL jitter | Cached values do not all expire at exactly the same moment |
| Cache invalidation | Updates and deletes remove old cached values |
| Pagination | Large lists are returned in smaller, safer pages |
| Health endpoint | Deployment systems can check whether the API is alive |
| Non-root container | The process does not run as the powerful root user |

## Why this can scale

- Async FastAPI handlers avoid blocking the event loop.
- PostgreSQL is the durable source of truth.
- SQLAlchemy uses connection pooling for concurrent requests.
- Redis serves repeated item reads without hitting PostgreSQL every time.
- Missing IDs are cached briefly to reduce cache penetration.
- Cache TTL jitter spreads expirations instead of expiring everything together.
- Updates and deletes invalidate affected cache keys.
- Pagination limits prevent unbounded list queries.
- The container runs as a non-root user.
- The API is stateless, so multiple replicas can run behind a load balancer.

## Deploy With Docker Compose

This is the easiest deployment for a server, test environment, or demonstration.

### 1. Install Docker

Install Docker Desktop locally or Docker Engine on a Linux server.

### 2. Start the service

```bash
cd scalable_crud_api
docker compose up -d --build
```

### 3. Check the service

```bash
curl http://localhost:8000/health
```

Expected response:

```json
{"status":"ok","cache":"redis"}
```

### 4. View logs

```bash
docker compose logs -f api
```

### 5. Stop the service

```bash
docker compose down
```

To remove the local database volume too, use `docker compose down -v`.

## Deploy For Real Traffic

For a production environment, use this shape:

```text
Users
	|
Load balancer / API gateway
	|
Multiple API containers
	|              |
PostgreSQL      Redis
```

The API containers should be identical and disposable. PostgreSQL and Redis should be managed services or highly available clusters. Add TLS at the load balancer, keep databases on private networks, and store passwords in a secrets manager.

Useful environment variables:

```bash
DATABASE_URL=postgresql+asyncpg://user:password@postgres-host:5432/app
REDIS_URL=redis://redis-host:6379/0
CACHE_TTL_SECONDS=60
NEGATIVE_CACHE_TTL_SECONDS=10
MAX_PAGE_SIZE=100
```

Never commit real passwords or connection strings to source control.

## Production upgrades still required

This sample is an architecture foundation, not a claim that one container handles millions of users. For a real deployment, add:

- Alembic migrations instead of `create_all`.
- Authentication, authorization, and rate limiting.
- OpenTelemetry, metrics, structured logs, and alerting.
- Managed PostgreSQL and Redis with backups, replicas, and failover.
- Kubernetes or another orchestrator with horizontal autoscaling.
- Load tests, contract tests, and security scanning.
- A distributed cache stampede lock for very hot keys.

The example uses `create_all` to keep local setup short. Production should create schema changes with versioned migrations before starting new application versions.

## Authentication API

The separate `auth_api.py` module demonstrates one API with several authentication levels. Run it with:

```bash
uvicorn auth_api:app --reload --port 8001
```

Open `http://localhost:8001/docs` to try the flows.

| Scheme | Best use | Endpoint |
|---|---|---|
| API key | Internal service-to-service calls | `GET /v1/items/api-key` |
| HTTP Basic | Simple protected admin tools over HTTPS | `GET /v1/items/basic` |
| OAuth2 password flow | Local development or a controlled first-party client | `POST /auth/token` |
| JWT bearer token | Stateless API authorization with scopes | `GET /v1/items/bearer` |
| OIDC/JWKS bearer token | Production login through Auth0, Keycloak, Okta, Cognito, or another identity provider | Same bearer endpoints |

### What each scheme means

- **API key:** a long secret sent in `X-API-Key`. It is simple, but it should be rotated and stored in a secrets manager.
- **HTTP Basic:** username and password sent with each request. Use only over HTTPS, and prefer it for limited internal tools.
- **OAuth2:** the client gets a short-lived access token instead of sending a password to every API endpoint.
- **JWT:** the token contains signed identity and scope information. The API verifies its signature, issuer, audience, and expiry.
- **OIDC/JWKS:** a professional identity provider issues tokens. The API validates them against the provider's public signing keys, so the API does not manage user passwords.
- **Scopes:** `items:read` and `items:write` limit what a token is allowed to do.

### Local authentication setup

Generate password hashes rather than storing plaintext passwords:

```bash
python -c 'from pwdlib import PasswordHash; print(PasswordHash.recommended().hash("change-me"))'
```

Set local variables before starting the auth API:

```bash
export JWT_SECRET='use-a-long-random-secret'
export SERVICE_API_KEY='replace-with-a-long-random-key'
export BASIC_AUTH_PASSWORD_HASH='paste-basic-password-hash'
export DEMO_PASSWORD_HASH='paste-demo-password-hash'
uvicorn auth_api:app --host 0.0.0.0 --port 8001
```

For production OIDC, configure the provider's issuer, JWKS URL, and audience:

```bash
export OIDC_ISSUER='https://identity.example.com/'
export OIDC_JWKS_URL='https://identity.example.com/.well-known/jwks.json'
export JWT_AUDIENCE='items-api'
```

Do not use the local password-token endpoint or default secrets in production. Use an external OIDC provider, short token lifetimes, key rotation, HTTPS, rate limiting, audit logs, and a secrets manager.
