from app.celery_worker import celery

@celery.task(name="agents.rules_agent")
def rules_agent(data: dict):
    customer = data.get("customer")
    
    if not customer:
        return {"action": "create_customer"}
    
    if customer["purchases"] > 5:
        return {"action": "offer_vip"}
    
    return {"action": "standard_flow"}