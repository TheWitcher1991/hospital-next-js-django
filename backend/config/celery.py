from __future__ import absolute_import, unicode_literals
import os

from celery import Celery, Task, current_app
from celery.result import AsyncResult
from celery.schedules import crontab
from celery.signals import after_setup_logger, after_setup_task_logger
from kombu import Queue, Exchange

from config.settings import DEBUG

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

MAX_TASK_PRIORITY = 10
DEFAULT_TASK_PRIORITY = 5
DEFAULT_EMAIL_TASK_PRIORITY = 10
DEFAULT_CELERY_RETRY = 3
DEFAULT_CELERY_RETRY_DELAY = 15

app.conf.worker_prefetch_multiplier = 1
app.conf.worker_max_tasks_per_child = 10
app.conf.task_acks_late = False

# TODO: может перенести на rabbitmq?
app.conf.broker_transport_options = {
    'priority_steps': list(range(MAX_TASK_PRIORITY)),
    'queue_order_strategy': 'priority',
    'visibility_timeout': 3600,
}

CELERY_QUEUE_DEFAULT = 'default'

app.conf.task_default_queue = CELERY_QUEUE_DEFAULT
app.conf.task_default_exchange_type = 'direct'
app.conf.task_default_routing_key = CELERY_QUEUE_DEFAULT

app.conf.task_queues = {
    Queue(
        CELERY_QUEUE_DEFAULT,
        Exchange(CELERY_QUEUE_DEFAULT),
        routing_key=CELERY_QUEUE_DEFAULT,
    ),
}

app.conf.task_routes = {}

app.conf.beat_schedule = {
    'check_expired_sessions': {
        'task': 'api.tasks.check_expired_sessions_task',
        'schedule': crontab(minute='*/120'),
        'options': {'queue': CELERY_QUEUE_DEFAULT},
    },
}


class BaseTaskWithRetry(Task):
    autoretry_for = (Exception, KeyError, TypeError)
    max_retries = DEFAULT_CELERY_RETRY
    default_retry_delay = DEFAULT_CELERY_RETRY_DELAY
    retry_backoff = True
    retry_jitter = False


@app.task
def check_task_result(task_id: str):
    """
    Проверяет результат задачи по её ID.
    """
    task_result = AsyncResult(task_id, app=current_app)

    if task_result.ready():
        return task_result.result
    return None


if DEBUG:
    @after_setup_logger.connect
    def setup_loggers(logger, *args, **kwargs):
        logger.info("Celery logger is set up.")


    @after_setup_task_logger.connect
    def setup_task_loggers(logger, *args, **kwargs):
        logger.info("Celery task logger is set up.")


app.conf.timezone = 'Europe/Moscow'
app.conf.enable_utc = True
