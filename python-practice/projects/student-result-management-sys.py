#student information
name = input('Enter Your Name: ')
age = int(input('Enter Your Age: '))
college = input('Enter College Name: ')
course = input('Enter Course Name: ')
marks = int(input('Enter Total Marks: '))

print('==========================')
print('     STUDENT DETAILS        ')
print('==========================')
print()

print(f'Name    : {name}')
print(f'Age     : {age}')
print(f'College : {college}')
print(f'Course  : {course}')
print(f'Marks   : {marks}')

#grade calculation

if marks >= 90: print('Grade : A')
elif marks >= 80: print('Grade : B')
elif marks >=60: print('Grade : C')
else: print('Fail')

#pass / fail

if marks >= 60: print('Status : Pass')
else: print('Status : Fail')

#voting eligibility

if age >=18: print('eligible to vote')
else: print('not eligible to vote')

#scholarship eligibility 

if marks >=90 and age >=22: print('Scholarship : Eligible')
else: print('Scholarship : Not Eligible')

#hostel eligibility

city = input('Do you live outside the city (yes/no): ').lower()
travel = int(input('Daily Travel Distance (km): '))

if city == 'yes' or travel >= 20: print('hostel eligibility : eligible')
else: print('hostel eligibility : not eligible')

#final report

print('==========================')
print('   STUDENT RESULT REPORT        ')
print('==========================')
print()

print(f'Name    : {name}')
print(f'Age     : {age}')
print(f'College : {college}')
print(f'Course  : {course}')
print(f'Marks   : {marks}')


if marks >= 90: print('Grade : A')
elif marks >= 80: print('Grade : B')
elif marks >=60: print('Grade : C')
else: print('Fail')



if marks >= 60: print('Status : Pass')
else: print('Status : Fail')


if age >+18: print('eligible to vote')
else: print('not eligible to vote')


if marks >=90 and age >=22: print('Scholarship : Eligible')
else: print('Scholarship : Not Eligible')


if city == 'yes' or travel >= 20: print('hostel eligibility : eligible')
else: print('hostel eligibility : not eligible')

