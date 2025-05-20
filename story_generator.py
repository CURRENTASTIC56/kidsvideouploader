# story_generator.py
from transformers import pipeline
import os

generator = pipeline("text-generation", model="gpt2")

def generate_story():
    prompt = "A magical bedtime story for kids about a talking rabbit who goes on an adventure"
    result = generator(prompt, max_length=300, do_sample=True, temperature=0.9)
    story = result[0]["generated_text"]
    
    os.makedirs("output", exist_ok=True)
    with open("output/story.txt", "w") as f:
        f.write(story)
    
    return story

def split_story(story):
    return [part.strip() for part in story.split(". ") if part.strip()]
