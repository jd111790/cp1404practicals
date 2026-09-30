"""
File Size prac
Loop that asks the user for a file name only ends when
the user enters an empty string
"""


def main():
    file_name = input("Enter filename: ")
    while file_name != "":
        print_file_size(file_name)
        file_name = input("Enter filename: ")


def print_file_size(file_name: str) -> int | None:
    try:
        in_file = open(file_name, "r")
        number_of_lines = len(in_file.readlines())
        print(f"File size is {number_of_lines} lines")
        in_file.close()
    except FileNotFoundError:
        print("File not found")


main()
