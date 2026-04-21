import streamlit as st
from gtts import gTTS
import io

text = "Hello, welcome to this course"
speech= gTTS(text, lang='en', slow=False)

# speech.save("welcome.mp3")

audio_buffer = io.BytesIO()
speech.write_to_fp(audio_buffer)

# st.audio("welcome.mp3")
st.audio(audio_buffer)