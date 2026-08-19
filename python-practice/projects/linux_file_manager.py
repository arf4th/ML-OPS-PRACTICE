import os

menu = [
    "1. Show Current Directory",
    "2. List Directory Content",
    "3. Check Path",
    "4. Rename File",
    "5. Deleted File",
    "6. Create Directory",
    "7.Build File Path",
    "8. Exit"
]

while True:
    print()
    print('='*30)
    print('     LINUX FILE MANAGER')
    print('='*30) 
    
    for item in menu:
        print(item)
        
    user_input = int(input('select a option: '))
    if user_input == 1:
        print()
        print(f'Current Working Directory is: {os.getcwd()}')

    elif user_input == 2:
        lists = os.listdir()
        for list in lists:
            print(list)

    elif user_input == 3:
        path = input('enter file or directory name: ')
        if os.path.exists(path):
            print('path exist')
        else:
            print('path not exist')

    elif user_input == 4:
        old = input('enter old file name: ')
        new = input('enter new file name: ')
        if os.path.exists(old):
            os.rename(old, new)
            print('file successfully renamed')
        else:
            print('file does not exist try again')

    elif user_input == 5:
        delete = input('enter filename to delete: ')
        if os.path.exists(delete):
            os.remove(delete)
            print('file successfullt deleted')
        else:
            print('file does not found')


    elif user_input == 6:
        ask = input('enter directory name: ')
        os.mkdir(ask)
        print('directory successfully created')


    elif user_input == 7:
        filename = input('enter file name: ')
        curr_dir = os.getcwd()
        filepath = os.path.join(curr_dir, filename)
        print(filepath)


    elif user_input == 8:
        print('exiting file manager...')
        break

    else:
        print('invalid option try again')