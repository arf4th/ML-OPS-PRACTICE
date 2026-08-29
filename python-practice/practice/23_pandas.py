import pandas as pd


# exam1 = pd.Series([85, 72, 90, 68, 95])
# exam2 = pd.Series([90, 80, 88, 75, 92])
# exam1.name = 'students_marks'
# exam2.name = 'students_marks'
# index = ['Arfath', 'Rahul', 'Priya', 'Aisha', 'Vijay']
# exam1.index = index
# exam2.index = index
# exam1['Aisha'] = 75
# print(f"Priya: {exam1['Priya']}")
# print(f"First Student: {exam1.iloc[0]}")

# exam1.iloc[1] = 80
# result = exam1 + exam2
# print(result)


# data = { 
#     "Name":["Arfath", "Rahul", "Priya", "Aisha", "Vijay"],
#     "Age":[22, 21, 23, 20, 24],
#     "Course":["Python", "Linux", "Python", "Devops", "Linux"],
#     "Marks":[85, 72, 90, 68, 95]
# }


# df = pd.DataFrame(data)

# print(df)



data = {
    "Name":["Arfath", "Rahul", "Priya", "Aisha", "Vijay", "Sana"],
    "Age":[22, 25, 28, 24, 30, 26],
    "Department":["Devops", "Linux", "Data", "Devops", "Data", "Linux"],
    "Salary":[45000, 55000, 70000, 50000, 85000, 60000],
    "Experience":[1, 3, 5, 2, 7, 4]
}

df = pd.DataFrame(data)

# print(df)

# print(df.loc[df.index == 'Priya'])

# print(df.iloc[0:4, [0, 3]])


# print(df.drop("Experience", axis=1))

# hike = df["Salary"] + 5000

# print(hike)

rename = df.rename(columns= {"Department": "Team", "Salary": "Monthly_Salary"})

print(rename)