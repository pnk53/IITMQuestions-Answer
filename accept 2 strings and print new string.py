print('Enter two strings: ')
str1 = str(input('Enter 1st string: '))
str2 = str(input('Enter 2nd string: '))
'''for c in str1:
        if(c in str2):
            str2 = str2.replace(c,'')
print(str2)'''
output = ''
for c in str2:
    if c not in str1:
        output = output + c

print(output)