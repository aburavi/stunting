# gunicorn_conf.py
import os
import json
from app.config import settings
import multiprocessing

# Bind to all interfaces on port 8000 (adjust as needed)
bind = f"{settings.HOST}:{settings.PORT}"

# Number of workers: (2 * cores) + 1 is a common formula for optimal performance
workers = (multiprocessing.cpu_count() * 2) + 1

# Worker class (sync is default; consider 'gevent' or 'eventlet' for async apps)
#worker_class = "sync"
worker_class = "uvicorn.workers.UvicornWorker"

# Worker timeout in seconds
timeout = settings.WORKERS_TIMEOUT
keepalive = settings.KEEPALIVE

# Maximum number of requests a worker will process before restarting
max_requests = settings.WORKERS_MAX_REQUESTS
max_requests_jitter = settings.WORKERS_REQUESTS_JITTER  # Randomize restarts to avoid all workers restarting at once

# Logging
accesslog = settings.ACCESSLOG  # Log access to stdout
errorlog = settings.ERRORLOG   # Log errors to stdout
loglevel = settings.LOGLEVEL if not settings.DEBUG else "debug"

# Daemon mode (set to False to run in foreground — recommended for containers)
daemon = False

# Reload on code changes (useful for development, disable in production)
reload = settings.DEBUG

# Graceful restart settings
graceful_timeout = settings.GRACEFUL_TIMEOUT

# Set the worker temporary directory (optional)
# worker_tmp_dir = "/dev/shm"

# Limit the number of simultaneous clients (per worker)
worker_connections = settings.MAX_WORKERS

# Note: For production, you may want to set:
# - accesslog and errorlog to actual file paths
# - daemon = True (if not running in container)
# - reload = False
# - Consider using 'gthread' or async workers if your app supports it

# For debugging and testing
log_data = {
    "loglevel": loglevel,
    "workers": workers,
    "bind": bind,
    "graceful_timeout": graceful_timeout,
    "timeout": timeout,
    "keepalive": keepalive,
    "errorlog": errorlog,
    "accesslog": accesslog,
    # Additional, non-gunicorn variables
    "workers_per_core": workers,
    "use_max_workers": settings.MAX_WORKERS,
    "host": settings.HOST,
    "port": settings.PORT,
}
print(json.dumps(log_data))