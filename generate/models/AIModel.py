import os

import requests
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

class AIModel:
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls(
                name= "stabilityai/stable-diffusion-xl-base-1.0",
                endpoint=os.getenv("COLAB_API_URL", ""),
                is_active=True
            )
        return cls.__instance
    
    def __init__(self, name: str, endpoint: str, is_active: bool = True):
        self.__name = name
        self.__endpoint = endpoint
        self.__is_active = is_active
    
    def create_image(self, prompt: str) -> bytes | None:
        try:
            response = requests.post(self.__endpoint, json={"prompt": prompt})
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            logger.error(f"Lỗi khi gọi API Colab: {e}")
            return None