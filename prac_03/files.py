# 1.

name_file = open("name.txt", "w")
user_name = input("What is your name? ")
print(user_name, file=name_file)

name_file.close()
