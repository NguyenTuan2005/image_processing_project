from datetime import datetime
from enum import Enum
from typing import Optional

from generate.models.AIModel import AIModel
from generate.models.Prompt import Prompt
from image.models.Image import Image

class MessageType(Enum):
    REQUEST = "request"
    RESPONSE = "response"

class ImageMessage:

    def __init__(self, message_id: str, message_type: MessageType, prompt: Prompt, status: str,
                 created_at: datetime, version: int):
        self.__message_id = message_id
        self.__message_type = message_type
        self.__prompt = prompt
        self.__status = status
        self.__created_at = created_at
        self.__version = version
        self.__image: Optional[Image] = None
        self.__ai_model: Optional[AIModel] = AIModel.get_instance()

    def submit(self, prompt: Prompt) -> Optional['ImageMessage']:
        self.__prompt = prompt
        self.__status = "pending"
        image_bytes = self.__ai_model.create_image(prompt.get_prompt_text())
        return image_bytes #Convert soon

    def cancel(self) -> None:
        self.__status = "cancelled"

    def check_status(self) -> str:
        return self.__status

    def get_generated_image(self) -> Optional[Image]:
        return self.__image
