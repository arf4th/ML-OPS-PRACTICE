# print("="*30)
# print("     PYTHON CALCULATOR")
# print("="*30)

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def divi(num1, num2):
    return num1 / num2

menu = [
    "1. Addition",
    "2. Substraction",
    "3. Multiplication",
    "4. Division",
    "5. Exit"
]

user_input = ""

while user_input != 5:

    print("="*30)
    print("     PYTHON CALCULATOR")
    print("="*30)


    print()

    for item in menu:
        
        print(item)

    print()

    user_input = int(input("Select Option: "))


    if user_input == 1:

                print("Addittion Seleted")
                
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))

                result = add(num1, num2)
                print(f"Addition is {result}")

    elif user_input == 2:
                
                print("Substraction Seleted")

                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))

                result = sub(num1, num2)
                print(f"Substraction is {result}")

    elif user_input == 3:

                print("Multiplcation Seleted")

                
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))

                result = mul(num1, num2)
                print(f"Multiplcaton {result}")

    elif user_input == 4:

                print("Division Seleted")

                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))

                result = divi(num1, num2)
                print(f"Division {result}")
        
    elif user_input == 5:

                print("Thanks for using python CLI Calculator.")
                
    else:
                print("Invalid Input")


