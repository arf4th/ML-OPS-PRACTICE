import pandas as pd


exam1 = pd.Series([85, 72, 90, 68, 95])
exam2 = pd.Series([90, 80, 88, 75, 92])
exam1.name = 'students_marks'
exam2.name = 'students_marks'
index = ['Arfath', 'Rahul', 'Priya', 'Aisha', 'Vijay']
exam1.index = index
exam2.index = index
# exam1['Aisha'] = 75
# print(f"Priya: {exam1['Priya']}")
# print(f"First Student: {exam1.iloc[0]}")

# exam1.iloc[1] = 80
result = exam1 + exam2
print(result)