import streamlit as st
from user.auth import login_user, register_user
from components import disease_predictor, treatment_generator, patient_chatbot
import pandas as pd

st.set_page_config(page_title="🏥 HealthAI", layout="centered", page_icon="🧠")

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Login"
if "username" not in st.session_state:
    st.session_state["username"] = ""
if "password" not in st.session_state:
    st.session_state["password"] = ""

# -------------------
# LOGIN PAGE
# -------------------
def login_page():
    st.markdown("<h2 style='text-align:center;'>🔐 Login to HealthAI</h2>", unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        if login_user(username, password):
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.session_state["password"] = password  # ⚠️ Store password (for internal use only)
            st.success(f"✅ Welcome, {username}!")
            st.session_state["current_page"] = "Home"
            st.rerun()
        else:
            st.error("❌ Invalid username or password.")

    st.info("Don't have an account?")
    if st.button("Create New Account"):
        st.session_state["current_page"] = "Register"

# -------------------
# REGISTER PAGE
# -------------------
def register_page():
    st.markdown("<h2 style='text-align:center;'>🆕 Register to HealthAI</h2>", unsafe_allow_html=True)

    new_user = st.text_input("New Username")
    new_pass = st.text_input("New Password", type='password')

    if st.button("Register"):
        if login_user(new_user, new_pass):
            st.warning("⚠️ Account already exists. Please login.")
        else:
            register_user(new_user, new_pass)
            st.success("✅ Account created! Please log in.")
            st.session_state["current_page"] = "Login"
            st.rerun()

    if st.button("Back to Login"):
        st.session_state["current_page"] = "Login"
        st.rerun()

# -------------------
# MAIN APP (Sidebar Navigation)
# -------------------
def main_app():
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/3774/3774299.png", width=100)
        st.markdown(f"### Welcome, {st.session_state['username']}")
        page = st.selectbox("Navigate", ["Patient Chat", "Disease Prediction", "Treatment Plan", "Logout"])

    if page == "Logout":
        st.session_state["authenticated"] = False
        st.session_state["current_page"] = "Login"
        st.session_state["username"] = ""
        st.session_state["password"] = ""
        st.rerun()

    elif page == "Patient Chat":
        st.header("🩺 Ask Your Medical Query")
        query = st.text_area("Type your question:")
        if st.button("Ask AI Doctor"):
            reply = patient_chatbot.get_chat_response(query, st.session_state["username"])
            st.success(reply)

    elif page == "Disease Prediction":
        st.header("🦠 Disease Prediction")
        symptoms = st.text_area("Enter symptoms")
        profile = st.text_input("Health history (optional)")
        if st.button("Predict"):
            result = disease_predictor.predict_disease(symptoms, profile, st.session_state["username"])
            st.success(result)

    elif page == "Treatment Plan":
        st.header("💊 Personalized Treatment")
        condition = st.text_input("Medical condition")
        profile = st.text_input("Additional health info")
        if st.button("Generate Plan"):
            plan = treatment_generator.generate_treatment(condition, profile, st.session_state["username"])
            st.success(plan)


# -------------------
# Routing Logic
# -------------------
if not st.session_state["authenticated"]:
    if st.session_state["current_page"] == "Login":
        login_page()
    elif st.session_state["current_page"] == "Register":
        register_page()
else:
    main_app()


