from datetime import datetime
from typing import List, Optional
from models.Image import Image
from models.AIModel import AIModel

class Prompt:

    def __init__(self, prompt_id: str, text: str):
        self.prompt_id = prompt_id
        self.text = text
    
    def edit_text(self, new_text: str) -> None:
        self.text = new_text
    
    def get_prompt_text(self) -> str:
        return self.text

class ImageRequest:
   
    def __init__(self, request_id: str, prompt: Prompt, status: str, 
                 created_at: datetime, version: int):
        self.request_id = request_id
        self.prompt = prompt
        self.status = status
        self.created_at = created_at
        self.version = version
        self.image: Optional[Image] = None
        self.ai_model: Optional[AIModel] = None
    
    def submit_request(self, prompt: Prompt, image_request: 'ImageRequest') -> None:
     
        self.prompt = prompt
        self.status = "pending"
    
    def cancel_request(self) -> None:
        self.status = "cancelled"
    
    def check_status(self) -> str:

        return self.status
    
    def get_generated_image(self) -> Optional[Image]:
        return self.image


class GenerationHistory:
    def __init__(self, chat_id: str, user, created_at: datetime):
        self.chat_id = chat_id
        self.user = user
        self.created_at = created_at
        self.image_requests: List[ImageRequest] = []
    
    def add_record(self, user, request: ImageRequest) -> None:
        self.image_requests.append(request)




