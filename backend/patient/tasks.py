from config.celery import BaseTaskWithRetry, app


@app.task(bind=True, base=BaseTaskWithRetry)
def create_patient_balance_task(self, patient_id: int) -> None:
    from .models import PatientBalance

    try:
        PatientBalance.objects.create(patient_id=patient_id, balance=0)
    except Exception as e:
        raise Exception(e)
