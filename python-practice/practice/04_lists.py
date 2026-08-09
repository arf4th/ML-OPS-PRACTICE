print('=========================')
print('     STUDENT SKILLS      ')
print('=========================')
print()

#AddingSkills
skills = ['Linux', 'Git', 'Python', 'Docker', 'AWS']
print(f'All Skills  : {skills}')

print(f'First Technology    : {skills[0]}')
print(f'Third Technology   : {skills[2]}')
print(f'Last Technology     : {skills[-1]}')

print('Updated Skills')
print()
skills[1] = 'GitHub'
print(skills)
print('Updated Skills')
print()
skills.extend(['Terraform', 'Kubernetes'])
print(skills)
print()
print('Updated Skills')
skills.remove('Python')
print(skills)
print()
print(f'Total Skills    : {len(skills)}')
print(f'First Skill     : {skills[0]}')
print(f'Last Skill      : {skills[-1]}')