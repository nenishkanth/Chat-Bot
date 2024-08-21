import streamlit as st
import google.generativeai as genai

st.title("Welcome to Generative AI")

genai.configure(api_key="AIzaSyDOifuuqTuy25bgfa3rDQ9awxAFoCABdyc")
text = st.text_input("Enter your prompt: ")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)