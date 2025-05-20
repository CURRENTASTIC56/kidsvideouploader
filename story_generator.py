from transformers import pipeline

def generate_story(prompt="Write a long kids story about animals learning teamwork"):
    generator = pipeline("text-generation", model="gpt2")
    story = generator(prompt, max_length=1000, do_sample=True)[0]['generated_text']
    return story
