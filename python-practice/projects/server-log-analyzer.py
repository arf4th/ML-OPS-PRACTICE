logs = [
    "INFO Server started successfully",
    "ERROR Database connection failed",
    "WARNING CPU usage high",
    "INFO User login successful",
    "ERROR Disk space full",
    "INFO Backup completed",
    "WARNING Memory usage high",
    "ERROR Network connection failed",
]


print('=============================')
print('    SERVER LOG REPORT')
print('=============================')
print()

print('All Logs')
print()

for i in logs:
    print(i)

print('=============================')
print('        LOG SUMMARY')
print('=============================')
print()

info_count = 0 
warning_count = 0 
error_count = 0

for log in logs:
    if 'INFO' in log:
        info_count += 1

    elif 'WARNING' in log:
        warning_count += 1
    elif 'ERROR' in log:
        error_count += 1

print(f'Total Logs      : {len(logs)}')
print(f'INFO Logs       : {info_count}')
print(f'WARNING Logs    : {warning_count}')
print(f'ERROR Logs      : {error_count}')
print()

errors = []

for log in logs:
    if 'ERROR' in log:
        errors.append(log)

print('ERROR REPORT:')
print()


for error in errors:
    print(error)

print()

warnings = []

for log in logs:
    if "WARNING" in log:
        warnings.append(log)

print('WARNING REPORT:')
print()

for warning in warnings:
    print(warning)

print()

error_types = set()

for log in logs:
    if "ERROR" in log:
      type = log.split()[1]
    error_types.add(type)

print('ERROR CATEGORIES:')
print(error_types)

print()

error_count = 0

for log in logs:
    if "ERROR" in log:
        error_count += 1

if error_count > 3:
    print("Server Status: Critical")
else:
    print("Server Status: Healthy")

print()

keyword = input('Enter keyword to search in logs: ').lower()

print('Search Result:')

for log in logs:

    if keyword in log.lower():
        print(log)

print()

print('==========================')
print('    SERVER HEALTH REPORT        ')
print('==========================')
print()


print(f'Total Logs      : {len(logs)}')
print()
print(f'INFO Count      : {info_count}')
print()
print(f'WARNING Count   : {warning_count}')
print()
print(f'ERROR Count     : {error_count}')
print()
print()

print('Error Messages:')
print(errors)
print()
print('Warning Messages:')
print(warning)
print()
print('Error Categories:')
print(error_types)
print()
print('Server Status')
print(error_count)