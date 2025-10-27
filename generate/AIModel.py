class AIModel:
    
    def __init__(self, name: str, api_key: str, endpoint: str, is_active: bool = True):
        self.name = name
        self.api_key = api_key
        self.endpoint = endpoint
        self.is_active = is_active
    
    def method(self, type: str) -> str:
        return type

print("AIModel module loaded successfully.")