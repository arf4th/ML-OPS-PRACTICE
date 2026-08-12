# with open('practice.txt', 'w') as file:
#     file = file.write('Linux\nPython\nMLOps')


# with open('practice.txt', 'r') as file:
#     file = file.read()

# content = file

# print(content)

# with open('practice.txt', 'a') as file:

#     file = file.write('\nDocker')

    

# with open('practice.txt', 'r') as file:
#     file = file.read()

# content = file

# print(content)



# with open('practice.txt', 'r') as file:
#     content = file.readline()
#     content2 = file.readline()
# print(content)
# print(content2)


# with open('practice.txt', 'r') as file:
#     content = file.readlines()

# for line in content:
#     print(line)


with open('practice.txt', 'r') as file:

    for line in file:
        print(line)