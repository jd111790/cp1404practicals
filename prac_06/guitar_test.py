from prac_06.guitar import Guitar

guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar_2 = Guitar("Another Guitar", 2013, 20.0)

print(guitar_1)
print(guitar_2)
print(f"guitar_1 get_age() - Expected 104. Got {guitar_1.get_age()}")
print(f"guitar_2 get_age() - Expected 13. Got {guitar_2.get_age()}")
print(f"104-year old guitar is_vintage() - Expected True. Got {guitar_1.is_vintage()}")
print(f"13-year old guitar is_vintage() - Expected False. Got {guitar_2.is_vintage()}")

"""
name = "Gibson L-5 CES"
year = 1922
cost = 16035.40
print(f"My guitar: {name}, first made in {year}")
"""