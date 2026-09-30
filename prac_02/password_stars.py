"""Module docstring"""


# imports
# CONSTANTS
MINIMUM_CHARACTERS = 8
def main():
    """Function docstring"""
    password = get_password(MINIMUM_CHARACTERS)

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
