from django.utils import timezone

from api.models import Session
from api.utils import queryset_ids
from config.celery import BaseTaskWithRetry, app


@app.task(bind=True, base=BaseTaskWithRetry)
def create_patient_balance_task(self, patient_id: int) -> None:
    from api.models import PatientBalance

    try:
        PatientBalance.objects.create(patient_id=patient_id, balance=0)
    except Exception as e:
        raise Exception(e)


@app.task(bind=True, base=BaseTaskWithRetry)
def check_expired_sessions_task(self) -> None:
    try:
        expired_sessions = Session.objects.filter(refresh_token_expires__lt=timezone.now()).values_list("id", flat=True)
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
