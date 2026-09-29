# 1.
out_name_file = open("name.txt", "w")
user_name = input("What is your name? ")
print(user_name, file=out_name_file)

out_name_file.close()

# 2.
in_name_file = open("name.txt", "r")
name = in_name_file.readline()
print(f"Hi {name.strip()}!")
in_name_file.close()

