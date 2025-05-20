# video_creator.py
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
import os

def create_scene_clip(image_path, audio_path, index):
    clip = ImageClip(image_path, duration=AudioFileClip(audio_path).duration)
    clip = clip.set_audio(AudioFileClip(audio_path))
    clip = clip.set_duration(AudioFileClip(audio_path).duration)
    clip = clip.resize(height=720)
    
    path = f"output/scenes/scene_{index}.mp4"
    clip.write_videofile(path, fps=24)
    return path

def create_final_video(scene_paths):
    final = concatenate_videoclips([ImageClip(p) for p in scene_paths])
    final.write_videofile("output/final_video.mp4", fps=24)
