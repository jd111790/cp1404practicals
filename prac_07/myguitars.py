"""
write a program that reads the data from guitars.csv
and stores them in a list of Guitar objects using the class

csv format in name, year, cost
"""
from prac_07.guitar import Guitar

FILE_NAME = "guitars.csv"


def main():
    guitars = read_file()
    for guitar in guitars:  # debugging
        print(guitar)
    guitars.sort()
    for guitar in guitars:  # debugging
        print(guitar)


def read_file():
    in_file = open(FILE_NAME, "r")
    return store_data_in_list(in_file)


def store_data_in_list(in_file):
    guitars = []
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    return guitars


main()
