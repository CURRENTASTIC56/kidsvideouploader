# image_generator.py
import os
from diffusers import StableDiffusionPipeline
import torch

# Load model once (slow on CPU)
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    revision="fp16",
    torch_dtype=torch.float16,
    use_auth_token=True
)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def generate_image(prompt, index):
    os.makedirs("output/images", exist_ok=True)
    image = pipe(prompt).images[0]
    path = f"output/images/scene_{index}.png"
    image.save(path)
    return path
