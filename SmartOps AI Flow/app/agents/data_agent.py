from app.celery_worker import celery
from app.services.db_service import get_customer_by_email

@celery.task(name="agents.data_agent")
def data_agent(data: dict):
    email = data.get("email")
    customer = get_customer_by_email(email)
    return {"customer": dict(customer) if customer else None}