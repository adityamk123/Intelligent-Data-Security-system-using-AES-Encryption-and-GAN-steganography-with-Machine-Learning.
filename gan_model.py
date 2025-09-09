from diffusers import StableDiffusionPipeline
import torch

def generate_image(prompt="A cyberpunk city at night, ultra realistic, 4k"):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model_id = "runwayml/stable-diffusion-v1-5"

    # Load pipeline
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32
    )
    pipe = pipe.to(device)

    # Generate image
    image = pipe(prompt).images[0]
    image.save("generated.png")
    return image
