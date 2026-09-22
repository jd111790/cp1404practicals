"""Module docstring"""


# imports
# CONSTANTS

def main():
    """Function docstring"""
    minimum_characters = 8
    password = get_password(minimum_characters)

    print_stars(password)


def print_stars(password: str):
    print("*" * len(password))


def get_password(minimum_characters: int) -> str:
    password = input(f"Enter Password (minimum {minimum_characters} characters): ")
    while len(password) < minimum_characters:
        print(f"password must be a mimimum of {minimum_characters} characters")
        password = input(f"Enter Password (minimum {minimum_characters} characters): ")
    return password


main()
