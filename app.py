import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

try:
    api_key = os.environ["GOOGLE_API_KEY"]
except KeyError:
    st.error("Google API Key not found in environment variables. Please set the GOOGLE_API_KEY environment variable.")
    st.stop()
    

genai.configure(api_key=api_key)

model= genai.GenerativeModel("gemini-2.5-pro")

st.set_page_config(
    page_title="Q&A Chatbot", 
    page_icon="🤖"
    )

st.title("Q&A Chatbot")
st.caption("Simple Chatbot powered by Google Gemini Pro")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "bot", "content": "Hello! How can I help you today?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input using the chat_input widget
if prompt := st.chat_input("What is up?"):
    # Add user message to session state and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- Generate and display AI response ---
    with st.chat_message("bot"):
        message_placeholder = st.empty()
        full_response = ""
        try:
            # Send the prompt to the model
            response = model.generate_content(prompt)
            # For this simple model, we get the whole response at once.
            full_response = response.text
            message_placeholder.markdown(full_response)

        except Exception as e:
            st.error(f"An error occurred: {e}")
            full_response = "Sorry, I encountered an error."
            message_placeholder.markdown(full_response)
    
    # Add the AI's response to the chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

