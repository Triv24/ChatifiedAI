import streamlit as st
from other import init_session, show_chat, add_message, gemini_chat, openai_chat, groq_chat, init_theme, apply_theme

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

st.title("👋🏻 Heyy!")
st.header("What can I do for you Today ? 😊")

model = st.selectbox(
    "Select a model:",
    ["gemini-2.5-flash", "gpt-4o", "gpt-5", "groq-4"],
    index=["gemini-2.5-flash", "gpt-4o", "gpt-5", "groq-4"].index(st.session_state.chat_model),
    key="chat_model"
)



if prompt := st.chat_input("Ask Here..."):
    add_message("chat_history", "user", prompt)
    
    if model == "gemini-2.5-flash":
        try:
            reply = gemini_chat(st.session_state.chat_history)
        except Exception as e:
            reply = f"⚠️ Looks Like an Error: {e}"

    elif model in ["gpt-4o", "gpt-3", "gpt-5"]:
        try:
            reply = openai_chat(st.session_state.chat_history, model=model)
        except Exception as e:
            reply = f"⚠️ Looks Like an Error: {e}"

    elif model == "groq-4":
        try:
            reply = groq_chat(st.session_state.chat_history, model=model)
        except Exception as e:
            reply = f"⚠️ Looks Like an Error: {e}"

    else:
        reply = "Please select model"

    add_message("chat_history", "assistant", reply)

show_chat("chat_history")
