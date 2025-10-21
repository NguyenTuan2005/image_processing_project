import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

def generate_image_from_prompt(prompt):
    try:
        url = settings.COLAB_API_URL
        response = requests.post(url, json={"prompt": prompt})
        response.raise_for_status()  # Raise lỗi nếu không thành công
        return response.content  # Trả về binary của ảnh
    except requests.exceptions.RequestException as e:
        logger.error(f"Lỗi khi gọi API Colab: {e}")
        return None