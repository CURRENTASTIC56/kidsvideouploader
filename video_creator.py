from moviepy.editor import *

def create_video(audio_path, image_path, output_file):
    audio = AudioFileClip(audio_path)
    image = ImageClip(image_path).set_duration(audio.duration).set_audio(audio).resize(height=720)
    image.write_videofile(output_file, fps=24)
