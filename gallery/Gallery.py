from datetime import datetime
from typing import List

from image.models.Image import Image


class Gallery:
    
    def __init__(self, gallery_id: str, title: str, description: str, 
                 created_at: datetime, user):
        self.__gallery_id = gallery_id
        self.__title = title
        self.__description = description
        self.__created_at = created_at
        self.__user = user
        self.__images: List[Image] = []
    
    def add_image(self, image: Image) -> None:
        self.__images.append(image)
    
    def remove_image(self, image_id: str) -> None:
        self.__images = [img for img in self.__images if img.image_id != image_id]
    
    def list_images(self) -> List[Image]:
        
        return self.__images
    
    def update_title(self, new_title: str) -> None:
        self.__title = new_title
    
    def update_description(self, new_description: str) -> None:
        self.__description = new_description

