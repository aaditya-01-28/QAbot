import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from datetime import date 
load_dotenv() 

try:
    api_key = os.environ["GOOGLE_API_KEY"]
except KeyError:
    st.error("Google API Key not found. Please create a .env file with GOOGLE_API_KEY='your_key'")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-pro')


st.set_page_config(
    page_title="Q&A Bot",
    page_icon="🤖"
)
st.title("Simple Q&A Bot")
st.caption("A simple chatbot powered by Google Gemini")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! How can I help you today?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if "date" in prompt.lower() and "today" in prompt.lower():
        today_date = date.today().strftime("%A, %B %d, %Y")
        full_response = f"Today's date is {today_date}."
        
        with st.chat_message("assistant"):
            st.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

    else:
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            try:
                response = model.generate_content(prompt)
                full_response = response.text
                message_placeholder.markdown(full_response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
                full_response = "Sorry, I encountered an error."
                message_placeholder.markdown(full_response)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})