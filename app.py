import streamlit as st
import google.generativeai as genai

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("Gen-ai.jpeg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    .centered-content {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;  /* Full viewport height */
        text-align: center;
    }
    .stApp {
        background: transparent;
    }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Welcome to Generative AI")

genai.configure(api_key="AIzaSyDOifuuqTuy25bgfa3rDQ9awxAFoCABdyc")
text = st.text_input("Enter your prompt: ")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)
