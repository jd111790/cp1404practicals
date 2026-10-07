numbers = []
for i in range(5):
    numbers.append(int(input("Number: ")))
    print(numbers)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"the smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
average_of_numbers = sum(numbers)/len(numbers)
print(f"The average of the numbers is {average_of_numbers}")
