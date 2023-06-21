import streamlit as st
import edge_tts
import subprocess

st.write("""## TTS anything
         
         """)
txt = st.text_area("Write or paste a text bellow to convert it to audio", height=300)
choice_lang =  ['pt-BR-AntonioNeural', 'en-US-AriaNeural', 'it-IT-DiegoNeural', 'es-AR-ElenaNeural', 'fr-FR-HenriNeural']

# Create a dropdown menu using selectbox
selected_lang = st.selectbox('Select an option', choice_lang)
st.write(f'You chose {selected_lang}')


if st.button('Convert to audio'):
    subprocess.run(['edge-tts', '--voice', selected_lang, '--text', txt, '--write-media', 'test.mp3'])
    st.audio('test.mp3')

