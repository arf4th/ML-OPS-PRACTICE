class server:
    def __init__(self, name, ip, status):
        self.name = name
        self.ip = ip
        self.status = status
    def serverinfo(self):
        print(f"Server Name     : {self.name}")
        print(f"IP Address      : {self.ip}")
        print(f"Status          : {self.status}")

server1run = server("web-server", "192.168.1.10", "running")
server1stop = server("web-server", "192.168.1.10", "stopped")
server2run = server("db-server", "192.168.1.20", "running")
server2stop = server("db-server", "192.168.1.20", "stopped")

# print(server1.name)
# print(server2.ip)

# server1.serverinfo()
# server2.serverinfo()


menu = [
    "1. list all servers",
    "2. run server",
    "3. stop server",
    "4. exit"
]

user_input = ""

while user_input != 4:
    print("="*30)
    print(      "SERVER INFO")
    print("="*30)

    for item in menu:
        print(item)

    user_input = int(input("Select Option: "))

    if user_input == 1:

        server1run.serverinfo()

        print()

        server2run.serverinfo()

    elif user_input == 2:
        perform = input("enter server name to run: ").lower()
        if perform == "web-server":

            print("Starting server...")

            server1run.serverinfo()
        elif perform == "db-server":

            print("Starting server...")

            server2run.serverinfo()
        else:
            print("no server found..")

    elif user_input == 3:
        perform = input("enter server name to run: ").lower()
        if perform == "web-server":

            print("Stopping server...")

            server1stop.serverinfo()
        elif perform == "db-server":

            print("Stopping server...")

            server2stop.serverinfo()
        else:
            print("no server found..")

    elif user_input == 4:
        print("exiting...")

    else:
        print("invalid input")





