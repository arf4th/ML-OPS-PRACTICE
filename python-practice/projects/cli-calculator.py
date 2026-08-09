print("="*30)
print("      PYTHON CALCULATOR")
print("="*30)

menu = [
    "1. Addition",
    "2. Substraction",
    "3. Multiplication",
    "4. Division",
    "5. Exit"
]
user_input = ""
while user_input !=5:
    for item in menu:
            print(item)
    user_input = int(input("Select Option: "))

    if user_input == 1:
      print("Addition selected:")

    elif user_input == 2:
        print("Substraction Selected:")

    elif user_input == 3:
        print("Multiplication Selected:")

    elif user_input == 4:
        print("Division Selected")

    elif user_input == 5:
        print("Thank you for using python calculator ")
def add(num1, num2):
    return num1 + num2

print("Addition:")
print()

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add(num1, num2)

print(f'Addition of two numbers is: {result}')

def sub(num1, num2):
    return num1 - num2

print("Substraction:")
print()

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = sub(num1, num2)

print(f"Substraction of two numbers are: {result}")


def mul(num1, num2):
    return num1 * num2

print("Multiplication:")
print()

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print()

result = mul(num1, num2)

print(f"Multiplication of two numbers: {result}")


def divi(num1, num2):
    return num1 // num2

print("Division:")
print()

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print()

result = divi(num1, num2)

print(f"Division of two numbers: {result}")