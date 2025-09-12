import streamlit as st
from other import init_session, show_chat, add_message, get_openai_client, init_theme, apply_theme

init_theme()
init_session()

toggle = st.sidebar.toggle("🌗 Dark Mode", value=(st.session_state.get("theme_mode") == "dark"))

if toggle:
    st.session_state.theme_mode = "dark"
else:
    st.session_state.theme_mode = "light"

apply_theme()

st.sidebar.markdown("""
## ✨ Start Instant Chat :
---""")

st.sidebar.page_link("Chat.py", label="Instant Chat")

st.sidebar.page_link("VoiceChat.py", label="Instant Voice Chat")

st.sidebar.markdown("""
---""")

st.sidebar.markdown("""
## ✨ Generate Image :
---""")

st.sidebar.page_link("Images.py", label="Instant Gemini Chat")

st.title("🎤 Voice Chat")

st.header("Hello! 😊 ")

st.subheader("🎙️ Welcome to the Voice-based Chatified! ")

st.divider()

uploaded_file = st.file_uploader("Upload a voice file", type=["mp3", "wav", "m4a"])

if "voice" not in st.session_state:
    st.session_state.voice = uploaded_file

if uploaded_file is not None:
    st.success("File uploaded! Try writing a prompt")
    
    client = get_openai_client()

    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with open(uploaded_file.name, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )

    transcripted_text = transcript.text

    add_message("chat_history", "user", transcripted_text)

    if prompt:= st.chat_input("Ask about the voicenote here..."):

        add_message("chat_history", "user", prompt)

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=st.session_state["chat_history"]
        )
        reply = response.choices[0].message.content

        add_message("chat_history", "assistant", reply)

show_chat("chat_history")