from datetime import datetime
from typing import Optional

class Image:

    def __init__(self, image_id: str, image_path: str, format: str, 
                 resolution: str, size: int, seed: str, created_at: datetime):
        self.image_id = image_id
        self.image_path = image_path
        self.format = format
        self.resolution = resolution
        self.size = size
        self.seed = seed
        self.created_at = created_at
        self.tag: Optional[Tag] = None
    
    def download(self) -> bytes:
        with open(self.image_path, 'rb') as f:
            return f.read()
    
    def get_info(self) -> str:
        return f"Resolution: {self.resolution}, Size: {self.size}, Format: {self.format}"
    
    def resize(self, new_resolution: str) -> None:
        self.resolution = new_resolution
    
    def delete(self) -> None:
        pass


class Tag:
    def __init__(self, tag_id: str, name: str):
        self.tag_id = tag_id
        self.name = name
    
    def rename(self, new_name: str) -> None:
        self.name = new_name    