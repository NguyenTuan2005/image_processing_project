from datetime import datetime
from typing import List, Optional

class User:
  
    def __init__(self, user_id: str, username: str, email: str, 
                 password: str, created_at: datetime):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at
        self.galleries: List[Gallery] = []
        self.generation_history: Optional[GenerationHistory] = None
    
    def update_profile(self, new_email: str, new_password: str) -> None:
   
        self.email = new_email
        self.password = new_password
    
    def create_gallery(self, title: str, description: str) -> Gallery:
        gallery = Gallery(
            gallery_id=f"gal_{len(self.galleries)}",
            title=title,
            description=description,
            created_at=datetime.now(),
            user=self
        )
        self.galleries.append(gallery)
        return gallery
    
    def view_galleries(self) -> List[Gallery]:
        return self.galleries