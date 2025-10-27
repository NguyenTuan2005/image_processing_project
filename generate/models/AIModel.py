class AIModel:
    
    def __init__(self, name: str, api_key: str, endpoint: str, is_active: bool = True):
        self.__name = name
        self.__api_key = api_key
        self.__endpoint = endpoint
        self.__is_active = is_active
    
    def method(self, type: str) -> str:
        return type

print("AIModel module loaded successfully.")