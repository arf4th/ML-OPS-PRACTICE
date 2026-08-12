# class server:
#     def __init__(self, name, ip, status):
#         self.name = name
#         self.ip = ip
#         self.status = status
#     def serverinfo(self):
#         print(f"Server Name     : {self.name}")
#         print(f"IP Address      : {self.ip}")
#         print(f"Status          : {self.status}")

# server1run = server("web-server", "192.168.1.10", "running")
# server1stop = server("web-server", "192.168.1.10", "stopped")
# server2run = server("db-server", "192.168.1.20", "running")
# server2stop = server("db-server", "192.168.1.20", "stopped")

# # print(server1.name)
# # print(server2.ip)

# # server1.serverinfo()
# # server2.serverinfo()


# menu = [
#     "1. list all servers",
#     "2. run server",
#     "3. stop server",
#     "4. exit"
# ]

# user_input = ""

# while user_input != 4:
#     print("="*30)
#     print(      "SERVER INFO")
#     print("="*30)

#     for item in menu:
#         print(item)

#     user_input = int(input("Select Option: "))

#     if user_input == 1:

#         server1run.serverinfo()

#         print()

#         server2run.serverinfo()

#     elif user_input == 2:
#         perform = input("enter server name to run: ").lower()
#         if perform == "web-server":

#             print("Starting server...")

#             server1run.serverinfo()
#         elif perform == "db-server":

#             print("Starting server...")

#             server2run.serverinfo()
#         else:
#             print("no server found..")

#     elif user_input == 3:
#         perform = input("enter server name to run: ").lower()
#         if perform == "web-server":

#             print("Stopping server...")

#             server1stop.serverinfo()
#         elif perform == "db-server":

#             print("Stopping server...")

#             server2stop.serverinfo()
#         else:
#             print("no server found..")

#     elif user_input == 4:
#         print("exiting...")

#     else:
#         print("invalid input")




# class person:
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city
#     def personinfo(self):
#         print(f'name   : {self.name}')
#         print(f'age    : {self.age} ')
#         print(f'city   : {self.city}')

# person1 = person("arfath", "21", "kadapa")
# person2 = person("john", "22", "hyderabad")

# person1.personinfo()
# print()
# person2.personinfo()


# class Car:
#     def __init__(self, brand, model, speed):

#         self.brand = brand
#         self.model = model
#         self.speed = speed

#     def show_info(self):

#         print(f'brand: {self.brand}')
#         print(f'model: {self.model}')
#         print(f'speed: {self.speed}')

#     def accelerate(self):
        
#         self.speed += 10
#         print(f'new speed: {self.speed}')





# Car1 = Car("toyota", "supra", 50)

# print(f'Initial speed: {Car1.speed}')

# Car1.show_info()

# Car1.accelerate()
# Car1.accelerate()

# Car1.show_info()


# class BankAccount:
#     def __init__(self, owner, balance):

#         self.owner = owner
#         self.balance = balance

#     def show_balance(self):

#         print(f'Owner: {self.owner}')
#         print(f'Balance: {self.balance}')

#     def deposit(self, amount):
#         self.amount = amount

#         self.balance += self.amount
#         print(f'New balance: {self.balance}')

#     def withdraw(self, amount):
#         self.amount = amount
        
#         self.balance -= self.amount
#         print(f'withdraw {self.balance}')



# account1 = BankAccount("arfath", 5000)
# account2 = BankAccount("john", 10000)


# account1.show_balance()
# print()
# account1.deposit(1000)

# account2.show_balance()
# print()
# account2.withdraw(8000)

# account2.show_balance()



class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width



    def perimeter(self):
        return (self.length + self.width) * 2


Rectangle1 = Rectangle(10, 5)

area_result = Rectangle1.area()
perimeter_result = Rectangle1.perimeter()


print(f'area: {area_result}')
print(f'perimeter: {perimeter_result}')