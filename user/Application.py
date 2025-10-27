from datetime import datetime
from models.User import User

class Application:
    def __init__(self):
        self.users = set()
    
    def login(self, email: str, password: str) -> bool:
        for user in self.users:
            if user.email == email and user.password == password:
                return True
        return False
    
    def logout(self) -> None:
        pass
    
    def register(self, username: str, email: str, password: str) -> User:
        user = User(
            user_id=f"user_{len(self.users)}",
            username=username,
            email=email,
            password=password,
            created_at=datetime.now()
        )
        self.users.add(user)
        return user
