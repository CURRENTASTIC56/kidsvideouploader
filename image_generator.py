from diffusers import StableDiffusionPipeline
import torch
import os

def generate_image(prompt, output_path="generated_image.png"):
    # Load the pipeline with CPU settings
    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
        revision="fp32",  # Make sure it loads fp32 weights
        torch_dtype=torch.float32,
    )

    pipe = pipe.to("cpu")  # Ensure running on CPU

    # Generate the image
    image = pipe(prompt).images[0]
    image.save(output_path)

    return output_path
