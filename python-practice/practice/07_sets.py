skill = {
    "Linux",
    "Python",
    "Docker",
    "Python",
    "AWS"
}

print('==========================')
print('     SKILL SET      ')
print('==========================')
print()

print('Original Skills:')
print(skill)
print()
skill.add("kubernetes")
print('After Adding Kubernetes:')
print(skill)
print()
skill.remove("Docker")
print('After Removing Docker')
print(skill)
print()
print('Linux exist:')
print("Linux" in skill)
