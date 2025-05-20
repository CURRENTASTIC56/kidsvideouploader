# tts_engine.py
import pyttsx3
import os

def text_to_speech(text, index):
    os.makedirs("output/audio", exist_ok=True)
    filename = f"output/audio/scene_{index}.mp3"
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()
    return filename
