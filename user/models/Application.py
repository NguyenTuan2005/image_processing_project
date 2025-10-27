from datetime import datetime

from user.models.User import User

class Application:
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def __init__(self):
        if hasattr(self, "_initialized") and self._initialized:
            return
        self.__users = set()
        self._initialized = True
    
    def login(self, email: str, password: str) -> bool:
        for user in self.__users:
            if user.isSameEmail(email) and user.isSamePassword(password):
                return True
        return False
    
    def logout(self) -> None:
        pass
    
    def register(self, username: str, email: str, password: str) -> User:
        user = User(
            user_id=f"user_{len(self.__users)}",
            username=username,
            email=email,
            password=password,
            created_at=datetime.now()
        )
        self.__users.add(user)
        return user
