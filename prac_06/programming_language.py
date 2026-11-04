class ProgrammingLanguage:
    def __init__(self, name = "", typing = "", reflection = bool, year = 0 ):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing.lower() == "dynamic":
            return self.name
        return None

    def __str__(self) -> str:
        programming_language_string = f"{self.name}, {self.typing} Typing, First appeared in {self.year}"
        return programming_language_string

