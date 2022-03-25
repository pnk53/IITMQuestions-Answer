print('Enter a string: ')
string = str(input())
vowels = []
s = ['a','e','i','o','u']
for c in string:
    if (c == 'a' or
        c == 'e' or
        c == 'i' or
        c == 'o' or
        c == 'u'
        ):
        vowels.append(c)

if(vowels != ''):
    print(vowels)
else:
    print('None')
