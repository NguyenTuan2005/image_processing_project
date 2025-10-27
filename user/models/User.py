from datetime import datetime
from typing import List, Optional

from gallery.Gallery import Gallery
from generate.models.GenerationHistory import GenerationHistory

class User:
  
    def __init__(self, user_id: str, username: str, email: str, 
                 password: str, created_at: datetime):
        self.__user_id = user_id
        self.__username = username
        self.__email = email
        self.__password = password
        self.__created_at = created_at
        self.__galleries: List[Gallery] = []
        self.__generation_history: Optional[GenerationHistory] = None
    
    def update_profile(self, new_email: str, new_password: str) -> None:
        self.__email = new_email
        self.__password = new_password
    
    def create_gallery(self, title: str, description: str) -> Gallery:
        gallery = Gallery(
            gallery_id=f"gal_{len(self.__galleries)}",
            title=title,
            description=description,
            created_at=datetime.now(),
            user=self
        )
        self.__galleries.append(gallery)
        return gallery
    
    def view_galleries(self) -> List[Gallery]:
        return self.__galleries

    def isSameEmail(self, email: str) -> bool:
        return self.__email == email

    def isSamePassword(self, password: str) -> bool:
        return self.__password == password