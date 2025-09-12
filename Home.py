import streamlit as st
from other import init_theme, apply_theme

# Initialise with dark theme
init_theme()
toggle = st.sidebar.toggle("🌗 Dark Mode", value=(st.session_state.get("theme_mode") == "dark"))

if toggle:
    st.session_state.theme_mode = "dark"
else:
    st.session_state.theme_mode = "light"

apply_theme()


# --------------  Sidebar markdown to show in the app  --------------
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

# ------------- Home Page markdown ------------------------------------------
st.markdown("""
# ✨ Welcome to Chatified
---

### Your all-in-one multimodal AI chat assistant. Ask, explore, and create with the world’s top AI models — all in one place.
---
## 🚀 What You Can Do with Chatified

    💬 Chat with leading LLMs: Switch seamlessly between GPT, Gemini, Groq, and more.

    🖼️ Generate images: Turn descriptive prompts into AI-generated visuals.

    🎙️ Speak naturally: Use voice prompts to interact hands-free.

    📷 Upload images: Ask questions about your images and get instant insights.

    📚 Session history: Keep track of your conversations across sessions.\n\n          
                     
               
## 🎁 Bonus Features

    🔄 Switch models mid-conversation without losing context.

    🌍 Multilingual support to chat in your preferred language.

    🌓 Theme toggle: Switch between light & dark mode anytime.

---
## 🌟 Why Chatified?

> **Chatified brings the power of multimodal AI into a single intuitive interface, making it easier than ever to chat, create, and explore.**
---""")

# -------------- Call-to-action Buttons -------------------

st.header("🚀 Get Started :")
st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("Chat.py", label="💬 Start Instant Chat", icon="💬")

with col2:
    st.page_link("Images.py", label="🎨 Generate Images", icon="🎨")

with col3:
    st.page_link("VoiceChat.py", label="🎤 Voice Chat", icon="🎤")
