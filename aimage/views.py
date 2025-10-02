from django.shortcuts import render
import base64
from io import BytesIO
import torch
from diffusers import StableDiffusionPipeline

# Ban đầu chưa load model
pipe = None

def getPipeline():
    global pipe
    if pipe is None:
        pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5"
        ).to("cuda" if torch.cuda.is_available() else "cpu")
    return pipe


def index(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        if prompt:
            # Gọi model khi cần
            image = getPipeline()(prompt).images[0]

            buffer = BytesIO()
            image.save(buffer, format="PNG")
            img_str = base64.b64encode(buffer.getvalue()).decode()

            return render(request, "aimage/index.html", {
                "generated_image": f"data:image/png;base64,{img_str}",
                "prompt": prompt
            })
    return render(request, "aimage/index.html")
