import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import time

# Load the environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

client = OpenAI()

def get_oga_scholar_response(user_input):
    response = client.chat.completions.create(
        model="ft:gpt-4o-2024-08-06:personal::B8QmIcnz",
        messages=[
            {"role": "system", "content": "You are an advisor for Ikorodu students on scholarships available for Ikorodu indigenes and residents only."},
            {"role": "user", "content": user_input},
        ]
    )
    return response.choices[0].message.content

# Streamlit App
st.set_page_config(page_title="ỌGAScholar Chatbot", page_icon="🎓", layout="centered")


# App Title
st.markdown("<h1 style='text-align: center; color: #4CAF50; font-size: 50px;'>🎓 ỌGAScholar Chatbot</h1>", unsafe_allow_html=True)

# Load and display banner 
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image("logo.png")

# Chatbot Info
st.markdown(
    "<div style='text-align: center; font-size: 18px;'>"
    "<strong>ỌGAScholar</strong> is your AI-powered assistant for all things on Ikorodu Scholarships." "Get accurate, up-to-date information on available scholarships, eligibility criteria, "
    "and application processes. It is designed to empower Ikorodu indigenes and residents in accessing education opportunities effortlessly!" 
    "</div>", unsafe_allow_html=True
)

st.markdown("---")

# Disclaimer
st.markdown("⚠️ **Disclaimer:** AI can make mistakes. Please verify important information from official sources.")

# User input
user_message = st.text_input("Type your question here and press Enter:", placeholder="E.g., What scholarships are available for Ikorodu students?")

# Process response
if user_message:
    with st.spinner("Ọga is thinking..."):
        time.sleep(2)  # Simulate a slight delay for better UX
        response = get_oga_scholar_response(user_message)
    
    st.success("✅ ỌGAScholar's Response:")
    st.write(response)
    
# Footer
st.markdown("---")
st.markdown("*Built with Love ❤️ | Designed for Ikorodu Students* 🏆")
st.markdown("© 2025 Toheebat Tiletile. All rights reserved.")
