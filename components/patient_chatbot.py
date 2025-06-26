from config.ibm_config import query_granite
from db.connection import log_ai_interaction

def get_chat_response(query, username):
    prompt = f"""
You are a medically knowledgeable assistant. Only respond to the specific question below, and do not generate or follow up with additional questions.

Question: "{query}"

Answer:"""

    try:
        # Get AI response from IBM Granite
        response = query_granite(prompt=prompt).strip()

        # Log interaction to database
        log_ai_interaction(
            username=username,
            module="patient-chatbot",
            input_text=query,
            ai_response=response
        )

        return response

    except Exception as e:
        error_message = f"❌ Error: {e}"

        # Log error to database
        log_ai_interaction(
            username=username,
            module="patient-chatbot",
            input_text=query,
            ai_response=error_message
        )

        return error_message

