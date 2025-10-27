from datetime import datetime
from typing import Set

from image.models.Tag import Tag

class Image:

    def __init__(self, image_id: str, image_path: str, format: str, 
                 resolution: str, size: int, seed: str, created_at: datetime):
        self.__image_id = image_id
        self.__image_path = image_path
        self.__format = format
        self.__resolution = resolution
        self.__size = size
        self.__seed = seed
        self.__created_at = created_at
        self.__tags: Set[Tag] = set()
    
    def download(self) -> bytes:
        with open(self.__image_path, 'rb') as f:
            return f.read()
    
    def get_info(self) -> str:
        return f"Resolution: {self.__resolution}, Size: {self.__size}, Format: {self.__format}"
    
    def resize(self, new_resolution: str) -> None:
        self.__resolution = new_resolution
    
    def delete(self) -> None:
        pass
