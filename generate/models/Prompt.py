class Prompt:

    def __init__(self, prompt_id: str, text: str):
        self.prompt_id = prompt_id
        self.text = text

    def edit_text(self, new_text: str) -> None:
        self.text = new_text

    def get_prompt_text(self) -> str:
        return self.text