
# try:
#     number = int(input('enter a number: '))

# except ValueError:
#     print('Invalid input. please enter a number')
# else:
#     print(f'the number you entered is {number}')
# finally:
#     print('exiting..')



# try:
#     num1 = int(input("enter first number: "))
#     num2 = int(input("Enter second number: "))

#     result = (num1 / num2)

# except ValueError:
#     print('invalid input. enter a number')
# except ZeroDivisionError:
#     print('cannot divide by 0')
# else:
#     print(f'result {result}')
# finally:
#     print('done..')




# while True:
#     try:
#         num = int(input('Enter a number'))

#         if num == 0:
#             print('exiting..')
#             break

#         print(f'you entered {num}')

#     except ValueError:
#         print('invalid input. please enter a number')



# try:

#     ask = input("Enter File Name: ")
#     with open(f'{ask}', 'r') as file:
#         content = file.read()

#         print(content)
# except FileNotFoundError:
#     print('file not found')


try:
    ask = int(input('Enter your age: '))
    if ask >=18:
        print('Age Accepted.')
    else:
        raise ValueError('Age must be 18 or above')
except ValueError as e:
    print(e)