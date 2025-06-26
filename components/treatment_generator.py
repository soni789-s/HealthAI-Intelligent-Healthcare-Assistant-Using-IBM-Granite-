from config.ibm_config import query_granite
from db.connection import log_ai_interaction

def generate_treatment(condition, profile, username):
    prompt = f"""
Suggest a personalized treatment plan for a patient with the following condition:
Condition: {condition}
Additional Profile Info: {profile}

Respond in a clear, medically safe, and structured manner.
"""
    response = query_granite(prompt)
    log_ai_interaction(username, "treatment", condition + "; " + profile, response)
    return response
