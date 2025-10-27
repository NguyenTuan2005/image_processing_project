import datetime
import uuid

from django.http import HttpResponse

from generate.models.ImageMessage import ImageMessage, MessageType
from generate.models.Prompt import Prompt

def create_image(request):
    if request.method == "POST":
        prompt = Prompt(
            prompt_id=str(uuid.uuid4()),
            text=request.POST.get("prompt")
        )

        message = ImageMessage(
            message_id=str(uuid.uuid4()),
            message_type=MessageType.REQUEST,
            prompt=prompt,
            status='created',
            created_at=datetime.UTC,
            version=1
        )

        image_bytes = message.submit(prompt)
        return HttpResponse(image_bytes, content_type="image/png")
    return HttpResponse(status=405)