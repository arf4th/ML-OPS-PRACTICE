menu = [
    "1. Show All Logs",
    "2. Add New Logs",
    "3. Search Log",
    "4. Show Error Log",
    "5. Show Warning Log",
    "6. Log Statitics",
    "7. Generate Summary",
    "8. Exit"
]

user_input = ""

while user_input != 8:

    print()

    print("="*30)
    print("         LINUX LOG ANALYZER")
    print("="*30)

    print()


    for item in menu:
        print(item)

    user_input =int(input('Select Option: '))

    if user_input == 1:
        with open('server.log', 'r') as file:
            show_log= file.readlines()
        if user_input == 1:
            print('============== ALL LOGS ===============')
            for line in show_log:
                print(line.rstrip())

    elif user_input == 2:
        print('============== ADD NEW LOG ===============')
        print()
        print("1. INFO")
        print("2. WARNING")
        print("3. ERROR")
        type = int(input("Select type of log in no. : "))
        if type == 1:
            print(f"Select Log Type: {type} ")
            msg = input('Enter Log Message: ')
            with open('server.log', 'a') as file:
                new_log = file.write(f'\nINFO {msg}')
        elif type == 2:
            print(f"Select Log Type: {type} ")
            msg = input('Enter Log Message: ')
            with open('server.log', 'a') as file:
                new_log = file.write(f'\nWARNING {msg}')
        elif type == 3:
            print(f"Select Log Type: {type} ")
            msg = input('Enter Log Message: ')
            with open('server.log', 'a') as file:
                new_log = file.write(f'\nERROR {msg}')
        else:
            print('invalid input')

    elif user_input == 3:

        ask = input("Enter Log word you want to search: ").lower()

        found = False

        with open('server.log', 'r') as file:
            print("========== SEARCH RESULTS ==========")
            for line in file:
                if ask in line.lower():
                    print(line.rstrip())
                    found = True


        if found == False:
            print("no matching logs found.")

    elif user_input == 4:
        with open('server.log', 'r') as file:
            read = file.readlines()
            for line in read:
                if "ERROR" in line:
                    print(line.rstrip())

    elif user_input == 5:
        with open('server.log', 'r') as file:
            read = file.readlines()
            for line in read:
                if "WARNING" in line:
                    print(line.rstrip)

    elif user_input == 6:
        with open('server.log', 'r') as file:
            count = file.readlines()
            print("========== LOG STATISTICS ==========")
            print()
            info_log = []
            warning_log = []
            error_log = []
            for line in count:
                if "INFO" in line:
                   ilogs = info_log.append(line)
                if "WARNING" in line:
                    wlog = warning_log.append(line)
                if "ERROR" in line:
                    elog = error_log.append(line)

            print(f'Total Logs      : {len(count)}')
            print(f'INFO Logs       : {len(info_log)}')
            print(f'WARNING Logs    : {len(warning_log)}')
            print(f'ERROR Logs      : {len(error_log)}')

    elif user_input == 7:
            with open('server.log', 'r') as file:
                count = file.readlines()
                print("========== SERVER LOG SUMMARY ==========")
                print()
                info_log = []
                warning_log = []
                error_log = []
                for line in count:
                    if "INFO" in line:
                       ilogs = info_log.append(line)
                    if "WARNING" in line:
                        wlog = warning_log.append(line)
                    if "ERROR" in line:
                        elog = error_log.append(line)

                error_count = len(error_log)

                if error_count <=2:
                    status = "Healthy"

                elif error_count <=4:
                    status = "Warning"
                elif error_count >=5:
                    status = "Critical"
                    
    
                print(f'Total Logs      : {len(count)}')
                print(f'INFO Logs       : {len(info_log)}')
                print(f'WARNING Logs    : {len(warning_log)}')
                print(f'ERROR Logs      : {len(error_log)}')
                print(f'Server Status : {status}')

    elif user_input == 8:
        print('Exiting Log Analyzer...')


    else:
        print('Invalid Input Try Again.')