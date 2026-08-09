age = int(input('Enter Your Age: '))
print('Do You Have license?')
license = input('Enter "Yes Or No": ').lower()

if age >=18:
    if license == 'yes':
        print('Eligible To Drive')
    else:
        print('Not Eligible')
else:
    print('Not Eligible')