from celery import Celery
from app.config import REDIS_BROKER

celery = Celery(
    "smartops",
    broker=REDIS_BROKER,
    backend=REDIS_BROKER
)

celery.conf.task_routes = {
    "agents.*": {"queue": "agents_queue"}
}