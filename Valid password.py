print('Enter a password: ')
s = str(input())

if (
    8 <= len(s) <= 32 and
    s[0].isalpha() and                     #.isalpha() is used to find wheather the initial letter belongs to a-z $ A-Z.
    '/' not in s and
    '=' not in s and
    ' ' not in s and
    '\\' not in s and
    '\'' not in s and
    '\"' not in s
):
    print('Yes')
else:
    print('No')