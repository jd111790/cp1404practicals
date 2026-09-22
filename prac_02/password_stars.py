minimum_characters = 8
password = input(f"Enter Password (minimum {minimum_characters} characters): ")
number_of_characters = len(password)

while number_of_characters < minimum_characters:
    print(f"password must be a mimimum of {minimum_characters} characters")
    password = input(f"Enter Password (minimum {minimum_characters} characters): ")
    number_of_characters = len(password)

print("*" * number_of_characters)
