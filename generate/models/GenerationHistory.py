from datetime import datetime
from typing import List

from generate.models.ImageMessage import ImageMessage

class GenerationHistory:
    def __init__(self, chat_id: str, user, created_at: datetime):
        self.__chat_id = chat_id
        self.__user = user
        self.__created_at = created_at
        self.__image_messages: List[ImageMessage] = []
    
    def add_record(self, message: ImageMessage) -> None:
        self.__image_messages.append(message)




