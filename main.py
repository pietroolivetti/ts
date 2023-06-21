import streamlit as st
import edge_tts
import subprocess

st.write("""## TTS anything
         
         """)
txt = st.text_area("Write or paste a text bellow to convert it to audio", height=300)

#choice_lang =  ['pt-BR-AntonioNeural', 'en-US-AriaNeural', 'it-IT-DiegoNeural', 'es-AR-ElenaNeural', 'fr-FR-HenriNeural']
choice_lang =  {'Português': 'pt-BR-AntonioNeural', 'English': 'en-US-AriaNeural', 'Italiano': 'it-IT-DiegoNeural', 'Español': 'es-AR-ElenaNeural', 'Français': 'fr-FR-HenriNeural'}

# Create a dropdown menu using selectbox
selected_lang = st.selectbox('Select an option:', choice_lang)
st.write(f"You've selected: {selected_lang}")


if st.button('Convert to audio'):
    subprocess.run(['edge-tts', '--voice', choice_lang[selected_lang], '--text', txt, '--write-media', 'test.mp3'])
    st.audio('test.mp3')
    

