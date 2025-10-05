from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from PIL import Image, ImageDraw, ImageFont
import io, base64

def home(request):
    return render(request, 'imagine/index.html')

@csrf_exempt
def create_meme(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image')
        top_text = request.POST.get('top_text', '').upper()
        bottom_text = request.POST.get('bottom_text', '').upper()

        # Open uploaded image
        img = Image.open(image_file).convert("RGB")
        draw = ImageDraw.Draw(img)

        # Try to load a font, fallback to default
        try:
            font = ImageFont.truetype("arial.ttf", size=int(img.height / 10))
        except:
            font = ImageFont.load_default()

        # Text position
        w, h = img.size
        # Draw top text
        if top_text:
            text_w, text_h = draw.textsize(top_text, font=font)
            draw.text(((w - text_w) / 2, 10), top_text, fill="white", font=font, stroke_width=2, stroke_fill="black")

        # Draw bottom text
        if bottom_text:
            text_w, text_h = draw.textsize(bottom_text, font=font)
            draw.text(((w - text_w) / 2, h - text_h - 10), bottom_text, fill="white", font=font, stroke_width=2, stroke_fill="black")

        # Convert to base64
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode()

        return JsonResponse({"image_base64": img_str})

    return JsonResponse({"error": "POST method required"}, status=400)
