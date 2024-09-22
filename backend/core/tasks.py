from django.utils import timezone

from config.celery import BaseTaskWithRetry, app

from .models import Session
from .utils import mail, queryset_ids


@app.task(bind=True, base=BaseTaskWithRetry)
def mail_task(
    self,
    subject="next-hospital.com",
    message="",
    recipient="",
    fail_silently=False,
    **kwargs,
) -> None:
    try:
        mail(subject=subject, message=message, recipient=recipient, fail_silently=fail_silently, **kwargs)
    except Exception as e:
        raise Exception(e)


@app.task(bind=True, base=BaseTaskWithRetry)
def check_expired_sessions_task(self) -> None:
    try:
        expired_sessions = Session.objects.filter(refresh_token_expires__lt=timezone.now())
        delete_session_task.chunks([(session,) for session in queryset_ids(expired_sessions)], 15).apply_async()
    except Exception as e:
        raise Exception(e)


@app.task(bind=True, base=BaseTaskWithRetry)
def delete_session_task(self, session_id: int) -> None:
    try:
        session = Session.objects.get(id=session_id)
        session.user.is_online = False
        session.user.save()
        session.delete()
    except Exception as e:
        raise Exception(e)
