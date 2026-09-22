"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    if result == "Excellent":
        print(f"User score {score} is {result} \n You get a prize!")

    score = random.randint(0, 100)
    result = determine_result(score)
    if result == "Excellent":
        print(f"User score {score} is {result} \n You get a prize!")

    print(f"Random: {score} = {result}")

    # end_program = input("end: ").upper()
    #
    # while end_program != "Y":
    #     score = random.randint(0, 100)
    #     result = determine_result(score)
    #
    #     print(f"Random: {score} = {result}")
    #     end_program = input("end: ").upper()


def determine_result(score: float) -> str:
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
