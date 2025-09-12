import streamlit as st

# Import all pages
home_page = st.Page("Home.py", title="Home", icon="🏠")
chat_page = st.Page("Chat.py", title="Instant Chat", icon="💬")
image_page = st.Page("Images.py", title="Generate Images", icon="🎨")
voice_page = st.Page("VoiceChat.py", title="Voice Chat", icon="🎤")

# Navigation object
pg = st.navigation(
    
    [home_page, chat_page, image_page, voice_page],
    
    position='top',

    expanded=True
)

# Run the selected page
pg.run()
