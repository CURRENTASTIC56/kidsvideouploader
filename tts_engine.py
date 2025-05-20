import pyttsx3

def text_to_speech(text, output_file):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.save_to_file(text, output_file)
    engine.runAndWait()
