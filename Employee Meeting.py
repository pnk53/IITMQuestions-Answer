print('Enter employee IDs of 5 employee: ')
e1 = int(input('e1'))
e2 = int(input('e2'))
e3 = int(input('e3'))
e4 = int(input('e4'))
e5 = int(input('e5'))

if (
        (e1+e2) % 2 == 0 and
        (e2+e3) % 2 == 0 and
        (e3+e4) % 2 == 0 and
        (e4+e5) % 2 == 0 and
        (e5+e1) % 2 == 0
):
    print('Yes')

else:
    print('No')