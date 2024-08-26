from config.celery import app, BaseTaskWithRetry
from django.utils import timezone

from api.models import Session


@app.task(bind=True, base=BaseTaskWithRetry)
def check_expired_sessions_task(self) -> None | bool:
    try:
        expired_sessions = Session.objects.filter(refresh_token_expires__lt=timezone.now())
        for session in expired_sessions:
            session.delete()
            session.user.is_online = False
            session.user.save()
        return True
    except Exception as e:
        raise Exception(e)
