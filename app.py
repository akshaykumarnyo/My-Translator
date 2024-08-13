import streamlit as st
from googletrans import Translator

# Create a Translator object
translator = Translator()

def translate_text(text, target_language, source_language='auto'):
    try:
        translated = translator.translate(text, src=source_language, dest=target_language)
        return translated.text
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit UI
st.title("Google Translate Text Translator")

# Input text
text = st.text_area("Enter text to be translated:", "Hello, how are you?")

# Language options
source_language = st.selectbox("Select source language:", ["auto", "en", "es", "de", "fr", "it", "nl", "pl", "ru", "ja", "zh"], index=0)
target_language = st.selectbox("Select target language:", ["en", "es", "de", "fr", "it", "nl", "pl", "ru", "ja", "zh"], index=1)

if st.button("Translate"):
    translated_text = translate_text(text, target_language, source_language)
    if translated_text:
        st.write(f"**Original text:** {text}")
        st.write(f"**Translated text:** {translated_text}")
