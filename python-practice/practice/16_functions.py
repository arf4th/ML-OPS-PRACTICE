def add(a, b):
    return a + b


def sub(a, b):
    return a- b

menu = [
    "1. Addition",
    "2. Substraction",
    "3. Exit"
]

user_input = ""

while user_input != 3:
    
    print()

    print("="*30)
    print(      "SIMPLE CALCULATOR")
    print("="*30)

    for item in menu:
        print(item)
    user_input = int(input("Select Option: "))

    if user_input == 1:
        print("Selected Addition")

        a = int(input("Enter first number: "))
        a = int(input("Enter second number: "))

        result = add(a, a)

        print(result)

    elif user_input == 2:
        print("Selected Substraction")

        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        result = sub(a, b)

        print(result)

    elif user_input == 3:
        print("Thanks for using py calculator")
    

    else:
        print("invalid input")