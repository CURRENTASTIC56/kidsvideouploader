from moviepy.editor import *
import os

def generate_video(image_paths, audio_path, output_path="final_video.mp4"):
    clips = []

    # Each scene lasts ~15 seconds
    for image_path in image_paths:
        clip = ImageClip(image_path).set_duration(15).resize(height=720)
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")

    narration = AudioFileClip(audio_path)

    # Add background music
    background_music = AudioFileClip("assets/background_music.mp3").volumex(0.2)
    final_audio = CompositeAudioClip([background_music.set_duration(video.duration), narration])
    
    final_video = video.set_audio(final_audio)
    final_video.write_videofile(output_path, fps=24)
