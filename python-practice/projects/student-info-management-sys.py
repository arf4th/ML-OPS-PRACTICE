#student profile

student = {
    "Name":'Arfath',
    "Age": 21,
    "College":'SHDC',
    "Course":'BCA',
    "City":'Kadapa'
}

print('==========================')
print('     STUDENT PROFILE        ')
print('==========================')
print()

print(f'Name    : {student["Name"]}')
print(f'Age     : {student["Age"]}')
print(f'College : {student["College"]}')
print(f'Course  : {student["Course"]}')
print(f'City    : {student["City"]}')

#academic report

marks = [88, 78, 67, 69, 91]

print('==========================')
print('     ACADEMIC REPORT        ')
print('==========================')
print()

print(f'Subject 1   : {marks[0]}')
print(f'Subject 2   : {marks[1]}')
print(f'Subject 3   : {marks[2]}')
print(f'Subject 4   : {marks[3]}')
print(f'Subject 5   : {marks[4]}')
print()

print(f'Total Marks : {sum(marks)}')
print(f'Highest Marks : {max(marks)}')
print(f'Lowest Marks : {min(marks)}')
print(f'Average Marks : {sum(marks) / len(marks)}')

#fixed information

course_details = ("BCA", "3 Years", "5Th Semester")

print('==========================')
print('     COURSE DETAILS        ')
print('==========================')
print()

print(f'Course  : {course_details[0]}')
print(f'Duration  : {course_details[1]}')
print(f'Semester  : {course_details[2]}')

#skill management

skills = {
    "Linux",
    "Docker",
    "Python",
    "Git",
    "AWS",
    "Python"
}

print('==========================')
print('     SKILLS        ')
print('==========================')
print()

print('Current Skills:')
print(skills)
print()

skills.add("Kubernetes")
print('After Adding:')
print(skills)
print()

skills.remove("Git")
print('After Removing:')
print(skills)
print()

print('Linux Available:')
print("Linux" in skills)


print('=============================')
print('    STUDENT SUMMARY REPORT        ')
print('=============================')
print()

print(f'Name        : {student["Name"]}')
print(f'Course      : {student["Course"]}')
print(f'Semester    : {course_details[2]}')
print()

print('Marks:')
print(marks)
print()

print(f'Total Marks: {sum(marks)}')
print(f'Average Marks: {sum(marks) / len(marks)}')
print()

print('Skills:')
print(skills)
print()

print('Number Of Skills:')
print(len(skills))

print('=============================================================')