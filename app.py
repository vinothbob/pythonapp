import streamlit as st
from deep_translator import GoogleTranslator

# Language codes for translation
lang_map = {
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "English": "en"
}

# App Title
st.title("🌍 Text Translator + Voice")

text = st.text_area("Enter text to translate")

language = st.selectbox("Choose language", list(lang_map.keys()))

if st.button("Translate"):
    if text:
        lang_code = lang_map[language]
        translated = GoogleTranslator(source='auto', target=lang_code).translate(text)
        st.success(f"Translated: {translated}")

        # JavaScript TTS using browser
        st.markdown(f"""
        <script>
            var msg = new SpeechSynthesisUtterance("{translated}");
            msg.lang = "{lang_code}";
            window.speechSynthesis.speak(msg);
        </script>
        """, unsafe_allow_html=True)
    else:
        st.warning("Please enter some text.")
