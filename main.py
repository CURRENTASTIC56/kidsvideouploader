from story_generator import generate_story
from tts_engine import text_to_speech
from video_creator import create_video
from youtube_uploader import upload_to_youtube
import os

os.makedirs("output", exist_ok=True)

STORY_FILE = "output/story.txt"
AUDIO_FILE = "output/story_audio.mp3"
VIDEO_FILE = "output/final_video.mp4"
IMAGE_PATH = "assets/background.jpg"

story = generate_story()
with open(STORY_FILE, "w") as f:
    f.write(story)

text_to_speech(story, AUDIO_FILE)
create_video(AUDIO_FILE, IMAGE_PATH, VIDEO_FILE)
upload_to_youtube(VIDEO_FILE, title="Daily AI Kids Story")
