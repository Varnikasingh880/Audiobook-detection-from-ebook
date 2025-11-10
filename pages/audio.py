import os, io, time, pathlib
#os — helpers for interacting with the operating system (files, env vars).
#io — input/output helpers (streams, buffers).
#time — time functions (sleep, timestamps).
#pathlib — object-oriented path handling.
import streamlit as st     #use this to create the web UI.
import pyttsx3   #an offline text-to-speech library used to convert text into audio.
from pathlib import Path  #Path makes working with file paths cleaner and platform-independent.
import PyPDF2  #a library used to read PDFs and extract text from pages.


APP_DIR = Path("audio.py").parent   #app directory and output folder #Creates a Path called APP_DIR equal to the parent directory of the literal string "audio.py".
EBOOK_DIR = APP_DIR  
OUTPUT_DIR = APP_DIR / "outputs"

# Optiona: create output dir if it doesn't exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def read_pdf(path):
     text_chunks = []
     with open(path, "rb") as f:
         reader = PyPDF2.PdfReader(f)
         for page in reader.pages:
             text = page.extract_text()
             if text:
                 text_chunks.append(text)
     return "\n".join(text_chunks)



def text_to_audio(text, output_path="outputs/audiobook.wav"):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)   # words per minute
    engine.setProperty("volume", 1.0) # max volume
    engine.save_to_file(text, output_path)
    engine.runAndWait()
    return output_path


st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        color: white;
    }
    .main {
        background-color: rgba(0,0,0,0.7);
        padding: 20px;
        border-radius: 15px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 12px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #0072ff, #00c6ff);
        box-shadow: 0px 0px 10px #00c6ff;
    }
    .stTextArea textarea {
        background-color: #1e1e1e;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Audiobook Generator", page_icon="🎧")

st.title("📖 Audiobook Generator 🎧")
st.markdown("---")

pdf_path = Path("assets/alice in wonderland long.pdf")

if pdf_path.exists():
    st.success("✅ PDF file found!")
    text_content = read_pdf(pdf_path)

    with st.expander("Preview Text"):
        st.text_area("Extracted Text", value=text_content[:2000], height=300)

    if st.button("Generate Audio"):
        audio_file = text_to_audio(text_content, "outputs/alice.wav")
        st.success("✅ Audiobook generated successfully!")
        
        audio_bytes = open(audio_file, "rb").read()
        st.audio(audio_bytes, format="audio/wav")
        st.download_button("Download Audio", audio_bytes, file_name="alice.wav")
else:
    st.error("❌ PDF not found! Please check path.")


st.markdown("<h2 style='text-align: center'>THANK YOU🫂</h2>", unsafe_allow_html=True)
st.markdown("---")

