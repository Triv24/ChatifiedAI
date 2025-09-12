import streamlit as st
from other import init_session, add_message, show_chat, gemini_img_chat, openai_image, init_theme, apply_theme

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

st.title("🎨 Chat & Generate Images")

if "img" not in st.session_state:
    st.session_state.img = None

st.title("✨ Hey!")
st.markdown("""#### Want to Ask about an Image?
You can directly enter a prompt if you want to generate an image without having to upload an image.
            """)

file = st.file_uploader("", type=["jpg", "jpeg", "png"])

if file is not None:
    st.session_state.img = file
    st.success("✅ Image uploaded successfully!")

if st.session_state.img is not None:
    st.image(st.session_state.img, caption="Your uploaded image")
    st.write("You can now ask Gemini about this image 🚀")
else:
    st.info("No image uploaded !")

if prompt := st.chat_input("Ask me Here...") :
    if st.session_state.img :    
        add_message("chat_history", "user", prompt)

        reply = gemini_img_chat(st.session_state.img, "chat_history" )

        add_message("chat_history", "assistant", reply)
    
    else :
        add_message("chat_history", "user", prompt)
        reply = openai_image(prompt)
        add_message("chat_history", "assistant", reply)

show_chat("chat_history")

