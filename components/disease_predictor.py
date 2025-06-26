from config.ibm_config import query_granite
from db.connection import log_ai_interaction

def predict_disease(symptoms, history, username):
    prompt = f"""
You are a medical assistant AI. need to give only the medical responses

A patient has reported the following symptoms:
{symptoms}

Their medical history is:
{history}

Your task:
- Predict the most likely disease or condition based on the symptoms and history.
- Provide a brief and medically sound explanation (2–3 sentences).

Important:
- Only give one prediction.
- DO NOT include greetings, disclaimers, citations, or unrelated questions.
- Keep it concise and professional.

Response:
"""


    response = query_granite(prompt)
    log_ai_interaction(username, "disease_predictor", symptoms + "; " + history, response)
    return response