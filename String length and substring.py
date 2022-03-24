print('Enter a string: ')
string = str(input())
n = len(string)
if (n>3):
    if (n % 2 == 0):
        if (string[n-1] == '.'):
            word = string[:-1]
        else:
            word = string + '.'
    else:
        word = string

    print(word)
    l = int((len(word)-1)/2)
    substring = word[l-1 : l+2]
    print(substring)
else:
    print('Invalid input')

