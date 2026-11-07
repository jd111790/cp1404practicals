import datetime


class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    # def __str__(self):
    #     return f"{self.name} ({self.year}) : ${self.cost}"

    def __repr__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self) -> int:
        current_year = datetime.datetime.now().year
        age = current_year - self.year
        return age

    def is_vintage(self) -> bool:
        current_year = datetime.datetime.now().year
        age = current_year - self.year
        if age >= 50:
            return True

        return False
