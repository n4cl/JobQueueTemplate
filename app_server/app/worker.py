import os
import redis
import rq

RQ_REDIS_URL = "redis://redis_server"

with rq.Connection(redis.from_url(RQ_REDIS_URL)):
    worker = rq.Worker(['default'])
    worker.work()
