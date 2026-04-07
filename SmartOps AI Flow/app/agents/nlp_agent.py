from app.celery_worker import celery
from app.services.openai_service import generate_summary

@celery.task(name="agents.nlp_agent")
def nlp_agent(data: dict):
    text = data.get("description", "")
    summary = generate_summary(text)
    return {"summary": summary}