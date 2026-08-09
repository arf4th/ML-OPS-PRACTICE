print("=========================")
print("   NUMBER GUESSER")
print("=========================")
print()
print("Guess a number between 1 and 20")

secret_number = 13
attempts = 5

user_input = ""

while user_input != secret_number:
    print()
    print(f'Attempts Left: {attempts}')
    user_input = int(input("Enter Guess: "))
    attempts -= 1
    print()
    if attempts == 0:
        print("Maximum Attempts Reached")
        break
    if user_input == secret_number:
            print("WON!!")
