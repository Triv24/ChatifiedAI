# A file with functions that are to be used throughout the app

import streamlit as st
from google import genai
from openai import OpenAI
from groq import Groq
import base64
from google.genai import types

# Initialising the session states
def init_session():
    defaults = {
        "chat_history": [],
        "chat_model": "groq-4",
        "image_history": [],
        "image_model": "gemini-2.5-flash",
        "voice_history": [],
        "voice_model": "gemini-2.5-flash",
        "voice_mode": False, 
        "openai_api" : "" 
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


# --------- CHAT RELATED FUNCTIONS -----------------------------------------------

# Adds chat message to the history of chats
def add_message(history_key, role, content):
    st.session_state[history_key].append({"role": role, "content": content})

# Displays Chats
def show_chat(history_key):
    for msg in st.session_state[history_key]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# Establishes connection with Gemini Api client
def get_gemini_client():
    if "gemini_client" not in st.session_state:
        st.session_state["gemini_client"] = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    return st.session_state["gemini_client"]

# Produces and returns response from gemini client
def gemini_chat(history):

    client = get_gemini_client()

    contents = "\n".join(f"{x} : {y}" for chat in history for x,y in chat.items())

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents
    )

    return response.text

# Establishes Open AI API connection :
def get_openai_client():
    if "openai_client" not in st.session_state:
        st.session_state["openai_client"] = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    return st.session_state["openai_client"]

# Produces and returns response from OpenAI API
def openai_chat(history, model="gpt-4o"):

    client = get_openai_client()

    messages = []
    for msg in history:
        role = "user" if msg["role"] == "user" else "assistant"
        messages.append({"role": role, "content": msg["content"]})

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    return response.choices[0].message.content

# Establishes connection with Groq API
def get_groq_client():
  
    if "groq_client" not in st.session_state:
        st.session_state["groq_client"] = Groq(api_key=st.secrets["GROQ_API_KEY"])
    return st.session_state["groq_client"]

# Produces and returns response from Groq API
def groq_chat(history, model="groq-4"):
   
    client = get_groq_client()

    messages = []
    for msg in history:
        role = "user" if msg["role"] == "user" else "assistant"
        messages.append({"role": role, "content": msg["content"]})

    response = client.chat.completions.create(
        model="groq/compound",
        messages=messages
    )
    return response.choices[0].message.content


# ------------------- IMAGE RELATED FUNCTIONS ---------------------------------

# Image generation from prompt by dall-e-3 model
def openai_image(prompt):
    client = get_openai_client()
    
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024"
    )
    return response.data[0].url


# Respond with the context from uploaded image
def gemini_img_chat(image, history):
    client = get_gemini_client()

    if image is None:
        return "No Image uploaded !"

    else :
        binary_image = image.read()

        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents=[
                genai.types.Part.from_bytes(
                    data=binary_image,
                    mime_type='image/jpeg',
                ), history
            ]
        )

    return response.text


# ------------------------ THEME RELATED FUNCTIONS ------------------------------------

# Initialise the session state for theme
def init_theme():
    if "theme_mode" not in st.session_state:
        st.session_state.theme_mode = "light"

# Change theme after toggle
def toggle_theme():
    if st.session_state.theme_mode == "light":
        st.session_state.theme_mode = "dark"
    else:
        st.session_state.theme_mode = "light"
    apply_theme()

# Set configuration of the theme
def apply_theme():
    mode = st.session_state.theme_mode
    if mode == "dark":
        st._config.set_option("theme.base", "dark")
        st._config.set_option("theme.backgroundColor", "#0e1117")
        st._config.set_option("theme.primaryColor", "#83FDB2")
        st._config.set_option("theme.secondaryBackgroundColor", "#262730")
        st._config.set_option("theme.textColor", "#ffffff")
    else:
        st._config.set_option("theme.base", "light")
        st._config.set_option("theme.backgroundColor", "white")
        st._config.set_option("theme.primaryColor", "#59a2d6")
        st._config.set_option("theme.secondaryBackgroundColor", "#f0f2f6")
        st._config.set_option("theme.textColor", "#000000")
    

