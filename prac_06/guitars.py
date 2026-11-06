from prac_06.guitar import Guitar

"""Storing the guitars.
Input until returns blank
name:
year:
cost:
NAME (YEAR) : $COST added.
name: .....
blank

These are my guitars:
Guitar 1:  Fender Stratocaster (2014), worth $    765.40
Guitar 2:       Gibson L-5 CES (1922), worth $ 16,035.40 (vintage)
Guitar 3:        Line 6 JTV-59 (2010), worth $  1,512.90
"""


def main():
    guitars = []
    guitar_name = input("Name: ")

    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: "))
        guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(guitar)
        print(f"{guitar.name} ({guitar.year}) : ${guitar.cost} added.")
        guitar_name = input("Name: ")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


main()
