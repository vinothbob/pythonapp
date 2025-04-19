import streamlit as st
from gtts import gTTS
from deep_translator import GoogleTranslator

# Language codes
lang_map = {
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "English": "en"
}

st.title("🌍 Language Translator + Voice")

text = st.text_area("Enter text to translate")

language = st.selectbox("Choose language", list(lang_map.keys()))

if st.button("Translate and Speak"):
    if text:
        lang_code = lang_map[language]
        translated = GoogleTranslator(source='auto', target=lang_code).translate(text)
        st.success(f"Translated: {translated}")

        tts = gTTS(translated, lang=lang_code)
        tts.save("speech.mp3")

        audio_file = open("speech.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
    else:
        st.warning("Please enter some text.")
