from app.agents.nlp_agent import nlp_agent
from app.agents.data_agent import data_agent
from app.agents.rules_agent import rules_agent

def onboarding_flow(payload: dict):
    step1 = nlp_agent.delay(payload)
    step2 = data_agent.delay(payload)
    
    summary = step1.get()
    customer = step2.get()
    
    decision_payload = {**summary, **customer}
    decision = rules_agent.delay(decision_payload).get()
    
    return {
        "nlp": summary,
        "customer": customer,
        "decision": decision
    }