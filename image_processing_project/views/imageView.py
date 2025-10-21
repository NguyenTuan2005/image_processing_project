from django.shortcuts import render
from django.http import HttpResponse
from image_processing_project.services.imageService import generate_image_from_prompt

def image_generator(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        image_data = generate_image_from_prompt(prompt)
        if image_data:
            return HttpResponse(image_data, content_type="image/png")  # Trả về ảnh trực tiếp
        else:
            return render(request, "error.html", {"message": "Không tạo được ảnh. Thử lại nhé! 😔"})
    return render(request, "image/generator.html")  # Form để nhập prompt