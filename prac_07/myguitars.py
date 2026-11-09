"""
write a program that reads the data from guitars.csv
and stores them in a list of Guitar objects using the class

csv format in name, year, cost
"""
from prac_07.guitar import Guitar

FILE_NAME = "guitars.csv"


def main():
    guitars = read_file()
    sort_guitars_by_year(guitars)
    add_guitar(guitars)


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

def sort_guitars_by_year(guitars):
    guitars.sort()

def add_guitar(guitars):
    guitar_name = input("Name: ")
    guitar_year = int(input("Year: "))
    guitar_cost = float(input("Cost: "))

    guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
    # print(guitars) # debugging
    # for guitar in guitars: # debugging
    #     print(guitar)
    sort_guitars_by_year(guitars)
    # for guitar in guitars: # debugging
    #     print(guitar)



main()
