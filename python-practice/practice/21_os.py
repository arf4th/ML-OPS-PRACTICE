import os

# print(f'Current Directory:, {os.getcwd()}')


# lists = os.listdir()

# for list in lists:
#     print(list)


# os.mkdir('os_test')

# print('directory created')

# path = os.path.exists('os_test')
# if path == True:
#     print('directory exist')

# else:
#     print('directory does not exist')




# directories = ['logs', 'backups', 'reports']

# for directory in directories:
#     if not os.path.exists(directory):
#         os.mkdir(directory)
#         print(f'{directory}: created')

#     else:
#         print(f'{directory}: not created')


# path = os.path.exists('server.log')

# if path:
#     print(f'server.log exist')

# else:
#     print(f'server.log does not exist')

# oldName = 'old_name.txt'

# if not os.path.exists(oldName):
#     print('old_name.txt not found')

# else:
#     os.rename('old_name.txt', 'new_name.txt')
#     print('file renamed successfully')

# deleteFile = 'delete_me.txt'

# if not os.path.exists(deleteFile):
#     print('file not found')

# else:
#     os.remove(deleteFile)
#     print('file deleted successfully')



fileName = 'server.log'

curr_dir = os.getcwd()

filePath = os.path.join(curr_dir, fileName)

print(filePath)