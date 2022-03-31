print('Enter a string: ')
string = str(input()).lower()
#vowels = [None]
vowels = ''
s = ['a','e','i','o','u']
for c in string:
    if (c == 'a' or
        c == 'e' or
        c == 'i' or
        c == 'o' or
        c == 'u'
        ):
        #vowels.append(c)
        vowels = vowels + c

if(vowels != ''):
    print(vowels)
else:
    print('None')
