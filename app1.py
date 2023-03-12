import streamlit as st
import ctranslate2

# Set up the app's title and icon.
st.set_page_config(
    page_title="Transliteration App",
    page_icon="🤖",
)

# Define the app's header.
header = st.container()
with header:
    st.title("Welcome To OSINTG Backward Transliteration App For Assamese")
    st.write("Enter the romanized text in English and see it transliterated back to native Assamese")

# Define the container for the user input form.
form = st.container()
with form:
    text_input = st.text_input("Enter text to transliterate:")
    if st.button("Transliterate"):
        model_path = "/home/hemanta/PhD-FOLDER/2.Second-paper-work/TRANSLITERATION-DEMO/CTranslate-NMT-Web-Interface-main/enas_ctranslate2/"
        translator = ctranslate2.Translator(model_path)

        tokens = text_input.split()
        transliterated_tokens = []
        for token in tokens:
            chars = list(token)
            transliterated_chars = translator.translate_batch([chars])[0][0]["tokens"]
            transliterated_token = "".join(transliterated_chars)
            transliterated_tokens.append(transliterated_token)
        transliterated_text = " ".join(transliterated_tokens)

        st.write("Input Text: ", text_input)
        st.write("Transliterated Text:", transliterated_text)

# Define the container for the sample text.
sample_text = st.container()
with sample_text:
    with open("sample_transliterated_text.txt", "r", encoding="utf-8") as f:
        sample_text_contents = f.read()

    st.title("Sample Text")
    st.write(sample_text_contents)
    if st.button("Transliterate Sample Text"):
        model_path = "/home/hemanta/PhD-FOLDER/2.Second-paper-work/TRANSLITERATION-DEMO/CTranslate-NMT-Web-Interface-main/enas_ctranslate2/"
        translator = ctranslate2.Translator(model_path)

        tokens = sample_text_contents.split()
        transliterated_tokens = []
        for token in tokens:
            chars = list(token)
            transliterated_chars = translator.translate_batch([chars])[0][0]["tokens"]
            transliterated_token = "".join(transliterated_chars)
            transliterated_tokens.append(transliterated_token)
        transliterated_text = " ".join(transliterated_tokens)

        st.write("Transliterated Text:", transliterated_text)
