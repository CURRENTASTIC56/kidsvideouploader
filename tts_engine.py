import pyttsx3

def generate_narration(text, output_path="outputs/narration.mp3"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)  # slower
    engine.save_to_file(text, output_path)
    engine.runAndWait()
