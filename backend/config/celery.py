from __future__ import absolute_import, unicode_literals

import os

from celery import Celery, Task, current_app
from celery.result import AsyncResult
from celery.schedules import crontab
from celery.signals import after_setup_logger, after_setup_task_logger
from kombu import Exchange, Queue

from config.settings import DEBUG
from core.defines import CeleryQueue

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

MAX_TASK_PRIORITY = 10
DEFAULT_TASK_PRIORITY = 5
DEFAULT_EMAIL_TASK_PRIORITY = 10
DEFAULT_CELERY_RETRY = 3
DEFAULT_CELERY_RETRY_DELAY = 15

app.conf.worker_prefetch_multiplier = 1
app.conf.worker_max_tasks_per_child = 10
app.conf.task_acks_late = True

app.conf.broker_transport_options = {
    "visibility_timeout": 3600,
}

app.conf.task_default_queue = CeleryQueue.DEFAULT
app.conf.task_default_exchange_type = "direct"
app.conf.task_default_routing_key = CeleryQueue.DEFAULT
app.conf.task_queue_max_priority = MAX_TASK_PRIORITY
app.conf.task_default_priority = DEFAULT_TASK_PRIORITY


def create_celery_queue(name: str, priority=DEFAULT_EMAIL_TASK_PRIORITY):
    return Queue(name, Exchange(name), routing_key=name, queue_arguments={"x-max-priority": priority})


app.conf.task_queues = {
    create_celery_queue(CeleryQueue.DEFAULT),
    create_celery_queue(CeleryQueue.PATIENT),
    create_celery_queue(CeleryQueue.EMPLOYEE),
    create_celery_queue(CeleryQueue.BUSINESS, MAX_TASK_PRIORITY),
}

app.conf.task_routes = {
    "core.tasks.delete_session_task": {"queue": CeleryQueue.DEFAULT},
    "patient.tasks.create_patient_balance_task": {"queue": CeleryQueue.PATIENT},
    "business.tasks.cancel_expired_invoices_task": {"queue": CeleryQueue.BUSINESS},
    "business.tasks.payment_create_task": {"queue": CeleryQueue.BUSINESS},
    "business.tasks.payment_capture_task": {"queue": CeleryQueue.BUSINESS},
    "business.tasks.payment_cancel_task": {"queue": CeleryQueue.BUSINESS},
    "business.tasks.payment_find_one_task": {"queue": CeleryQueue.BUSINESS},
}

app.conf.beat_schedule = {
    "check_expired_invoices": {
        "task": "business.tasks.check_expired_invoices_task",
        "schedule": crontab(hour="0", minute="0"),
        "options": {"queue": CeleryQueue.BUSINESS},
    },
    "check_expired_sessions": {
        "task": "core.tasks.check_expired_sessions_task",
        "schedule": crontab(minute="*/120"),
        "options": {"queue": CeleryQueue.DEFAULT},
    },
}


class BaseTaskWithRetry(Task):
    autoretry_for = (Exception, KeyError, TypeError)
    max_retries = DEFAULT_CELERY_RETRY
    default_retry_delay = DEFAULT_CELERY_RETRY_DELAY
    retry_backoff = True
    retry_jitter = True


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
