import streamlit as st
from orchestrator.orchestrator import orchestrate
from voice_io.stt import transcribe_audio
from voice_io.tts import speak_text
import asyncio

st.title("📊 Finance Voice Assistant")

audio_file = st.file_uploader("Upload your question (audio)", type=["mp3", "wav"])
if audio_file:
    with open("temp.wav", "wb") as f:
        f.write(audio_file.read())

    query = transcribe_audio("temp.wav")
    st.success(f"You asked: {query}")

    answer = orchestrate(query)
    st.success(answer)

    if st.button("🔊 Speak Answer"):
        asyncio.run(speak_text(answer))
        st.audio("output.mp3")
