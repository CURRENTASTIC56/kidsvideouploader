from transformers import pipeline, set_seed

generator = pipeline("text-generation", model="distilgpt2")
set_seed(42)

def generate_story():
    prompt = "Write a short fun story for kids about a magical forest where animals talk."
    result = generator(prompt, max_length=150, num_return_sequences=1)
    story = result[0]['generated_text']
    return story.strip()
