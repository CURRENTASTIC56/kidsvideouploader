# main.py
from story_generator import generate_story, split_story
from tts_engine import text_to_speech
from video_creator import create_scene_clip, create_final_video
from image_generator import generate_image
from youtube_uploader import upload_to_youtube
import os

def main():
    story = generate_story()
    scenes = split_story(story)

    os.makedirs("output/scenes", exist_ok=True)

    video_paths = []
    for idx, scene in enumerate(scenes):
        print(f"Processing scene {idx + 1}/{len(scenes)}")
        image = generate_image(scene, idx)
        audio = text_to_speech(scene, idx)
        clip = create_scene_clip(image, audio, idx)
        video_paths.append(clip)

    create_final_video(video_paths)
    upload_to_youtube("output/final_video.mp4", title="AI Kids Story - Scene Visuals")

if __name__ == "__main__":
    main()