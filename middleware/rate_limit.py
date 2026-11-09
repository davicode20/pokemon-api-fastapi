from fastapi import Request, HTTPException
from cache.redis_client import redis_client

LIMIT = 10
WINDOW = 60  # estabelecendo segundos


async def rate_limit(request: Request):
    print("RATE LIMIT CHAMADO.")

    ip = request.client.host

    key = f"ratelimit:{ip}"

    current = redis_client.get(key)

    if current:
        if int(current) >= LIMIT:
            raise HTTPException(
                status_code=429, detail="Muitas requisições. Tente novamente mais tarde."
            )
        redis_client.incr(key)
    else:
        redis_client.set(key, 1, ex=WINDOW)
