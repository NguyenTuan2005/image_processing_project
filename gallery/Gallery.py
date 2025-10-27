from datetime import datetime
from typing import List
from models.Image import Image

class Gallery:
    
    def __init__(self, gallery_id: str, title: str, description: str, 
                 created_at: datetime, user):
        self.gallery_id = gallery_id
        self.title = title
        self.description = description
        self.created_at = created_at
        self.user = user
        self.images: List[Image] = []
    
    def add_image(self, image: Image) -> None:
        self.images.append(image)
    
    def remove_image(self, image_id: str) -> None:
        self.images = [img for img in self.images if img.image_id != image_id]
    
    def list_images(self) -> List[Image]:
        
        return self.images
    
    def update_title(self, new_title: str) -> None:
        self.title = new_title
    
    def update_description(self, new_description: str) -> None:
        self.description = new_description

