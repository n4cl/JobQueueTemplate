import redis
from rq import Queue
from print import test_print

RQ_REDIS_URL = "redis://redis_server"

q = Queue(connection=redis.from_url(RQ_REDIS_URL))

q.enqueue(test_print)
