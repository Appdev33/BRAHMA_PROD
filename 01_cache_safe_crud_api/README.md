# Cache-Safe CRUD API

This is a small FastAPI service for creating, reading, updating, and deleting items. It stores the real data in SQLite and uses Redis to make repeated reads faster.

The database is the source of truth. Redis is only a speed layer, so the API still works when Redis is unavailable.

## Quick Start

Install the packages:

```bash
pip install fastapi uvicorn redis
```

Start Redis locally, then run the API:

```bash
uvicorn cache_crud_api:app --reload
```

Open the interactive API page:

```text
http://127.0.0.1:8000/docs
```

The database file `cache_crud.db` is created automatically.

## Available Endpoints

| Method | URL | Purpose |
|---|---|---|
| `GET` | `/health` | Check whether the API and cache are available |
| `POST` | `/items` | Create an item |
| `GET` | `/items` | List items with pagination |
| `GET` | `/items/{id}` | Read one item |
| `PUT` | `/items/{id}` | Replace an item |
| `DELETE` | `/items/{id}` | Delete an item |

Example request:

```bash
curl -X POST http://127.0.0.1:8000/items \
  -H 'Content-Type: application/json' \
  -d '{"name":"Cache notes","description":"Revision material"}'
```

Example read:

```bash
curl http://127.0.0.1:8000/items/{id}
```

## Cache Problems Solved

### 1. Cache penetration

**Problem:** Many requests ask for data that does not exist. Every request reaches the database.

**Solution:** When an item is missing, the API briefly stores `{"missing": true}` in Redis. Repeated invalid requests are answered from Redis instead of repeatedly querying SQLite.

Code: `get_item()` uses `NEGATIVE_TTL`.

### 2. Cache stampede / thundering herd

**Problem:** A popular cache entry expires and thousands of requests query the database at the same time.

**Solution:** The first request obtains a short Redis lock and loads the item. Other requests wait briefly and then reuse the new cache value.

Code: `Cache.lock()`, `Cache.unlock()`, and `lock:{key}` in `get_item()`.

### 3. Cache avalanche

**Problem:** Many cache entries expire at exactly the same time, sending a large wave of traffic to the database.

**Solution:** Every cache lifetime receives a random extra delay, called TTL jitter. Expirations are spread over time.

Code: `Cache.set()` adds `random.randint(0, 10)` seconds.

### 4. Hot keys

**Problem:** One very popular item receives most of the traffic.

**Solution:** Frequently requested items are served from Redis, avoiding a database query for every request. The stampede lock also protects the database when that item expires.

Code: `item:{id}` cache keys and `get_item()`.

### 5. Cache inconsistency and stale data

**Problem:** The database changes but the old value remains in Redis.

**Solution:** After update or delete, the item cache is removed. After create, update, or delete, cached list pages are also removed.

Code: `cache.delete()` and `cache.clear_lists()` in the write endpoints.

### 6. Cache failure

**Problem:** Redis is down or temporarily unreachable.

**Solution:** Redis errors are caught. The API reads and writes directly to SQLite, so the service remains usable, although reads may be slower.

Code: `Cache.get()`, `Cache.set()`, `Cache.delete()`, and `Cache.clear_lists()`.

### 7. Cache eviction

**Problem:** Redis removes entries when it runs out of memory.

**Solution:** The API never treats a cache miss as data loss. A missing cache value simply causes a database read and a cache rebuild.

Code: every read path falls back to `db_get()` or `db_list()`.

### 8. Cache warming

**Problem:** After a restart, the cache is empty and the database receives the first burst of requests.

**Solution:** The first request automatically loads the item into Redis. This is lazy warming: only data that is actually requested is warmed.

Code: `cache.set()` after a successful database read.

## How The Code Is Organized

### Database layer

The `db_*` functions use SQLite:

- `db_create()` inserts an item.
- `db_get()` reads one item.
- `db_list()` reads a page of items.
- `db_update()` changes an item.
- `db_delete()` removes an item.

SQLite WAL mode allows readers and writers to work more safely under concurrent use.

### Cache layer

The `Cache` class hides Redis details from the endpoint code. It provides:

- `get()` to read cached data.
- `set()` to cache data with an expiry time.
- `delete()` to invalidate specific keys.
- `clear_lists()` to invalidate collection pages.
- `lock()` and `unlock()` to coordinate concurrent cache misses.

If Redis cannot be reached, these methods fail safely and the database remains available.

### API layer

The FastAPI endpoints validate input with Pydantic models:

- `ItemIn` limits name and description sizes.
- `Item` describes the complete stored object.
- `Page` describes paginated responses.

Pagination is limited to 100 records per request to prevent accidentally expensive queries.

## Configuration

The defaults work for local development. These environment variables can change them:

| Variable | Default | Meaning |
|---|---|---|
| `DATABASE_PATH` | `cache_crud.db` | SQLite database location |
| `REDIS_URL` | `redis://localhost:6379/0` | Redis connection URL |
| `CACHE_TTL_SECONDS` | `60` | Normal item cache lifetime |
| `NEGATIVE_CACHE_TTL_SECONDS` | `10` | Missing-item cache lifetime |

Example:

```bash
DATABASE_PATH=/data/items.db REDIS_URL=redis://redis:6379/0 \
  uvicorn cache_crud_api:app --host 0.0.0.0 --port 8000
```

## Important Production Notes

This code demonstrates the cache design and is suitable as a foundation. Before deploying at large scale:

- Replace SQLite with PostgreSQL or another shared production database.
- Add authentication and authorization.
- Add rate limiting, metrics, tracing, and structured logs.
- Use Redis high availability and configure memory eviction policies.
- Add database migrations and automated tests.
- Use HTTPS and restrict network access to Redis and the database.
