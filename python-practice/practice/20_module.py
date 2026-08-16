# import random

from datetime import datetime

curr_datetime = datetime.now()
curr_date = curr_datetime.date()
curr_time = curr_datetime.time()
curr_year = curr_datetime.year
curr_day = curr_datetime.day
curr_hour = curr_datetime.hour
curr_min = curr_datetime.minute
curr_sec = curr_datetime.second
curr_month = curr_datetime.month
print(f'current date and time: {curr_datetime}')
print(f'current date: {curr_date}')
print(f'current time: {curr_time}')
print(f'year: {curr_year}')
print(f'month: {curr_month}')
print(f'day: {curr_day}')
print(f'hour: {curr_hour}')
print(f'min: {curr_min}')
print(f'second: {curr_sec}')





# # print(number)



# choice = ["linux", "python", "docker", "git"]


# # print(random.choice(choice))


# # number = random.random()

# # range_values = 50 - 20

# # result = number * range_values

# # result = result + 10

# # uniform = random.uniform(10, 50)

# # print(f'random value: {uniform}')

# print(f"before: {choice}")

# shuffle = random.shuffle(choice)


# print(f'after: {choice}')

