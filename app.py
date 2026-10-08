
from prompts import( SYSTEM_PROMPT, WELCOME_MESSAGE_TEMPLATE, SUMMARY_REQUEST_PROMPT)

from google import genai
from google.genai import types
import streamlit as st
import requests
import re


GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
TELEGRAM_BOT_TOKEN = st.secrets["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = st.secrets["TELEGRAM_CHAT_ID"]

@st.cache_resource
def get_gemini_client():
    return genai.Client(api_key=GEMINI_API_KEY)

gemini_client = get_gemini_client()
MODEL_NAME = "gemini-3.5-flash"

def render_message(message):
    with st.chat_message(message["role"]):
        if message["kind"] == "text":
            st.write(message["content"])
        elif message["kind"] == "image":
            st.image(message["content"])
        

def add_message(role, kind, content):
    st.session_state.messages.append({"role": role, "kind": kind, "content": content})
    render_message(st.session_state.messages[-1])

def ask_gemini(parts):
    try:
        return st.session_state.chat.send_message(parts).text
    except Exception as error:
        return f"Sorry, something went wrong: {error}"


def clean_telegram_text(text):
    if not text:
        return "No summary available."

    # Remove markdown links: [text](url) → text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)

    # Remove markdown formatting
    text = text.replace("\\*", "")
    text = text.replace("**", "")
    text = text.replace("*", "")
    text = text.replace("__", "")
    text = text.replace("_", "")

    # Remove HTML tags if Gemini accidentally generates them
    text = re.sub(r'<[^>]+>', '', text)

    text = text.strip()
    return text[:4000] + "..." if len(text) > 4000 else text
 



def send_telegram(user_name, summary):
    try:
        text = clean_telegram_text(summary)
        response = requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": f"Hello {user_name}! Here's your study summary:\n\n{text}"
            }
        )
        return True, response.json().get("result", {}).get("message_id")
    except Exception as error:
        return False, str(error)



#step1- Onboarding

if "onboarderd" not in st.session_state:
    st.title("StudyBuddy - Your AI Study Companion")
    with st.form("onboarding_form"):
        name = st.text_input("Enter your name") 
        study_goal = st.text_input("What's your study goal? (Optional)")
        submitted = st.form_submit_button("Submit")

    if submitted:
        if not name.strip():
            st.warning("Please fill in your name before submitting.")
        else:
            st.session_state.name = name.strip()
            st.session_state.study_goal = study_goal.strip()
            st.session_state.chat = gemini_client.chats.create(
                model =MODEL_NAME,
                config = types.GenerateContentConfig(system_instruction = SYSTEM_PROMPT)
            )
            st.session_state.messages = []
            st.session_state.onboarderd = True
            st.rerun()

    st.stop()




# Create a Chat Interface

header_col, button_col = st.columns([5, 2], vertical_alignment="center")

with header_col:
    st.title("StudyBuddy - Your AI Study Companion")
    st.caption("Upload an image of your study material and get a concise summary!")

with button_col:
    send_disabled = len(st.session_state.messages) <= 2
    if st.button("📤 Send to Telegram", disabled=send_disabled, use_container_width=True):
        with st.spinner("Summarizing your day..."):
            summary = ask_gemini([SUMMARY_REQUEST_PROMPT])
        success, info = send_telegram(st.session_state.name, summary)
        if success:
            st.success("Sent! Check your Telegram 📲")
        else:
            st.error(f"Couldn't send that: {info}")
 
st.caption(f"Hello {st.session_state.name}! You can ask questions or upload images of your study material for a summary.")


if not st.session_state.messages:
    add_message("assistant", "text", WELCOME_MESSAGE_TEMPLATE.format(name=st.session_state.name))
else :
    for message in st.session_state.messages:
        render_message(message)

user_input = st.chat_input(
    "Ask a question or upload an image of your study material here...",
    accept_file = True,
    file_type = ["png", "jpeg", "jpg"])

if user_input:
    photo = user_input.files[0] if user_input.files else None
    text = user_input.text if user_input.text else None
    parts = []
    if photo is not None:
        photo_bytes = photo.getvalue()
        add_message("user", "image", photo_bytes)
        parts.append(types.Part.from_bytes(data=photo_bytes, mime_type=photo.type))
    if text is not None:
        add_message("user", "text", text)
        parts.append(types.Part.from_text(text= text))
    elif photo is not None:
        parts.append("Please summarize the uploaded image.")

    with st.spinner("Generating response..."):
        answer = ask_gemini(parts)
    add_message("assistant", "text", answer)