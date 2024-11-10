#imports
import numpy as np
import requests

#insult api stuff
insultAPI = requests.get("https://insult.mattbas.org/api/insult")
insult = insultAPI.text

#introduction
print("Welcome to the ToxicCalculator, where we do really just hate you.")

#taking the operation using a function for reusability
#checks if operation is valid or not
operation_types = ["+", "-", "*", "/"]
operation_taken = []

def take_input():
    operation_taken.append(str(input("Enter the operation you want to do (+, -, *, /): ")))
    return f"You have chosen: {operation_taken[-1]}"

print(take_input())

while operation_taken[-1] not in operation_types:
    print(f"{take_input()}")

#asking how many numbers to take

nums = [int(i) for i in input("Enter your numbers (/ and - operate the first number on all the others): ").split()]

#THE CALCULATOR STUFF
#every function returns both the insult + answer
class Calculator:
    @staticmethod
    def add(x):
        return f"{insult}Anyways the answer is {np.sum(x)}"

    @staticmethod
    def subtract(x):
        return f"{insult}Anyways the answer is {np.subtract(x, x[0])}"

    @staticmethod
    def multiply(x):
        return f"{insult}Anyways the answer is {np.prod(x)}"

    @staticmethod
    def divide(x):
        return f"{insult}Anyways the answer is {np.divide(x, x[0])}"

#ANSWER
#CHECKS INPUT AND GIVES AN ANSWER

if operation_taken[-1] == "+":
    print(Calculator.add(nums))
elif operation_taken[-1] == "-":
    print(Calculator.subtract(nums))
elif operation_taken[-1] == "*":
    print(Calculator.multiply(nums))
elif operation_taken[-1] == "/":
    print(Calculator.divide(nums))

