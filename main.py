import streamlit as st
import edge_tts
import subprocess

st.write("""## TTS anything
         
         """)
txt = st.text_area("Write or paste a text bellow to convert it to audio", height=300)

choice_lang =  {'Português': 'pt-BR-AntonioNeural', 'English': 'en-US-AriaNeural', 'Italiano': 'it-IT-DiegoNeural', 'Español': 'es-AR-ElenaNeural', 'Français': 'fr-FR-HenriNeural', 'Deutsch': 'de-DE-KillianNeural', 'Polski': 'pl-PL-ZofiaNeural'}

# Create a dropdown menu using selectbox
selected_lang = st.selectbox('Select a language:', choice_lang, index=0)
#st.write(f"You've selected: {selected_lang}")

choice_speed = {'Normal': '--rate=+1%', 'Very Slow': '--rate=-50%', 'Slow': '--rate=-25%', 'Fast': '--rate=+50%'}
selected_speed = st.selectbox('Speed: ', choice_speed, index=0)

if st.button('Convert to audio'):
    subprocess.run(['edge-tts',  choice_speed[selected_speed] ,'--voice', choice_lang[selected_lang], '--text', txt, '--write-media', 'tts.mp3'])
    st.audio('tts.mp3')
