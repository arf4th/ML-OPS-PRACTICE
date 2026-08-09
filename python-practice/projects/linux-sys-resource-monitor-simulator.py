menu = [
    "1. System Information",
    "2. CPU Monitor",
    "3. Memory Monitor",
    "4. Disk Monitor",
    "5. Show Running Processes",
    "6. Search Process",
    "7. System Health",
    "8. Monitoring Statistics",
    "9. Exit"
]

user_input = ""

while user_input != 9:

    print()

    print("="*30)
    print("         LINUX SYSTEM MONITOR")
    print("="*30)

    print()

    for item in menu:

        print(item)

    user_input = int(input("Select Option: "))

    print()

    if user_input == 1:
        print(f"Option {user_input} Selected")

        print()

        print("============== SYSTEM INFORMATION ===============")
        print()
        print("Hostname        : ubuntu-server")
        print()
        print("OS              : Ubuntu")
        print()
        print("Kernel          : 7.0.0-29")
        print()
        print("CPU Cores       : 8")
        print()
        print("Total RAM       : 16GB")
        print()
        print("Disk Capacity   : 512GB")

        print()

    elif user_input == 2:
        print(f"Option {user_input} Selected")
        
        print()
        
        print("============== CPU MONITOR ===============")
        print()

        print("CPU Usage     : 73%")
        print()
        print("Status        : High!!")

        print()

    elif user_input == 3:
        print(f"Option {user_input} Selected")
        
        print()
        
        print("============== MEMORY MONITOR ===============")
        print()

        print("Memory Usage : 64%")
        print()
        print("Status       : Normal")

        print()

    elif user_input == 4:
        print(f"Option {user_input} Selected")
                
        print()
                
        print("============== Disk Monitor ===============")
        print()

        print("Disk Usage       : 91%")
        print()
        print("Status           : Critical")

        print()

    elif user_input == 5:
        print(f"Option {user_input} Selected")
                        
        print()
                        
        print("============== SHOW RUNNING PROCESSES ===============")
        print()

        print(" PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+")
        print()
        print("3541 arfath    20   0 4959268 289648 148668 S  13.0   3.9   8:07.02")
        print("245      python          18%     4.5%        Running")
        print("312      firefox         25%     8.2%        Running")
        print("26800 arfath    20   0 1530688 135268  98120 S   5.3   1.8   0:05.57")
        print("294 root     -51   0       0      0      0 S   2.7   0.0   0:45.24 ")
        print("...")
        
        print()

    elif user_input == 6:
        print(f"Option {user_input} Selected")
                                
        print()

        psid = input("Enter Process Name: ")

        if psid == "python":
            print("Search Results:")
            print()
            print("PID      NAME            CPU     MEMORY      STATUS")
            print("245      python          18%     4.5%        Running")

        elif psid == "arfath":
            print("Search Results:")
            print()
            print(" PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+")
            print("3541 arfath    20   0 4959268 289648 148668 S  13.0   3.9   8:07.02")
            print("26800 arfath    20   0 1530688 135268  98120 S   5.3   1.8   0:05.57")

        elif psid == "root":
            print("Search Results:")
            print()
            print(" PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+")
            print("294 root     -51   0       0      0      0 S   2.7   0.0   0:45.24 ")

        elif psid == "firefox":
            print("Search Results:")
            print()
            print("PID      NAME            CPU     MEMORY      STATUS")
            print("312      firefox         25%     8.2%        Running")

        else:
            print("No matching processes found.")

            print()

    elif user_input == 7:
        print(f"Option {user_input} Selected")
                                
        print()

        print("========== SYSTEM HEALTH ==========")
        print()

        print("CPU       : High")
        print("Memory    : Normal")
        print("Disk      : Critical")
        print()
        print("Overall   : Critical")

        print()

    elif user_input == 8:
        print(f"Option {user_input} Selected")
                                
        print()

        print("========== MONITORING STATISTICS ==========")
        print()

        print("Total Processes       : 8")
        print("Running Processes     : 7")
        print("High CPU Processes    : 2")
        print("High Memory Processes : 3")
        print()

    elif user_input == 9:

        print("Exiting Linux System Monitor...")

    else:
        print("Invalid Option")

