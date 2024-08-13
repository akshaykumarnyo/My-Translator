import streamlit as st
from googletrans import Translator, LANGUAGES

# Create a Translator object
translator = Translator()

def translate_text(text, target_language, source_language='auto'):
    try:
        if target_language not in LANGUAGES or source_language not in LANGUAGES:
            raise ValueError("Selected language is not supported.")
        translated = translator.translate(text, src=source_language, dest=target_language)
        return translated.text
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit UI configuration
st.title("Google Translate Text Translator")


# Language selection
source_language = st.selectbox(
    "Select source language:",
    options=LANGUAGES.keys(),
    format_func=lambda x: LANGUAGES[x]
)
target_language = st.selectbox(
    "Select target language:",
    options=LANGUAGES.keys(),
    format_func=lambda x: LANGUAGES[x]
)

# Input text area
text = st.text_area("Enter text to be translated:", "Hello, how are you?")

# Translate button
if st.button("Translate"):
    translated_text = translate_text(text, target_language, source_language)
    if translated_text:
        st.write(f"**Original text:** {text}")
        st.write(f"**Translated text:** {translated_text}")

# Footer
st.markdown("""
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
        color: #888;
    }
    </style>
    <div class="footer">
        <p>Powered by Streamlit and Google Translate API</p>
    </div>
    """, unsafe_allow_html=True)
