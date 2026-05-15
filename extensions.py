import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# We pull the redis_url here so it's ready when the app starts
redis_url = os.getenv("REDIS_URL", "memory://")

limiter = Limiter(
    key_func=get_remote_address,
    storage_uri=redis_url,
    strategy="fixed-window"
)