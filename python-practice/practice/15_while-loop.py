count = 1 
while count <= 10:
    print(count)
    count +=1

count = 0
while count <=20:
    print(count)
    count +=2

count = 10
while count >= 0:
    print(count)
    count -=1

password = ""

while password != "python123":
    password = input('Enter password: ')
    print('Login Successful')
    

menu = [
        '1. Start Server',
        '2. Stop Server',
        '3. Restart Server',
        '4. Exit'
        ]


user_input = ''

while user_input != '4':

    print('===========MENU==========')
    print()

    for item in menu:
        print(item)

        print()

    user_input = input('Select a Number: ')

    print('exiting')


