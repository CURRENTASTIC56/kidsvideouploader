import os
from story_generator import generate_story
from image_generator import generate_image
from video_generator import generate_video
from tts_generator import generate_narration
from title_description_generator import generate_title_and_description

def split_story_into_scenes(story, scene_count=20):
    sentences = [s.strip() for s in story.split('.') if s.strip()]
    return sentences[:scene_count]

def main():
    print("Generating story...")
    story = generate_story()
    scenes = split_story_into_scenes(story)

    image_paths = []
    print("Generating images...")
    for i, scene in enumerate(scenes):
        image_path = f"outputs/scene_{i}.png"
        generate_image(scene, image_path)
        image_paths.append(image_path)

    print("Generating narration...")
    narration_path = "outputs/narration.mp3"
    generate_narration(story, narration_path)

    print("Generating video...")
    generate_video(image_paths, narration_path)

    print("Generating title and description...")
    title, description = generate_title_and_description(story)

    print("✅ Done!")
    print("Title:", title)
    print("Description:\n", description)

if __name__ == "__main__":
    os.makedirs("outputs", exist_ok=True)
    main()
