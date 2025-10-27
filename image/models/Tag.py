
class Tag:
    def __init__(self, tag_id: str, name: str):
        self.__tag_id = tag_id
        self.__name = name

    def rename(self, new_name: str) -> None:
        self.__name = new_name