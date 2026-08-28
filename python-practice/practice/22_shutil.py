import os
import shutil


# if os.path.exists(ask2):
#     shutil.copy2(ask1, ask2)
#     print(os.listdir(ask2))
#     print('file copied')

# else:
#     os.mkdir(ask2)
#     shutil.copy2(ask1, ask2)
#     print(os.listdir(ask2))
#     print('dir created and file copied')



# if os.path.exists(ask2):
#     shutil.move(ask1, ask2)
#     print(os.listdir(ask2))
#     print('file moved')

# else:
#     os.mkdir(ask2)
#     shutil.move(ask1, ask2)
#     print(os.listdir(ask2))
#     print('dir created and moved')





# dire = 'project_files/logs'

# os.makedirs(dire)

# open('project_files/server.log', 'w').close()
# open('project_files/config.txt', 'w').close()
# open('project_files/logs/error.log', 'w').close



ask1 = input('enter source dir name : ')
ask2 = input('enter dir name to copy into: ')


if os.path.exists(ask2):
    print('dire already exist')

else:
    shutil.copytree(ask1, ask2)
    print(os.listdir(ask2))
    print('dir copied successfully')