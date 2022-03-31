print('Enter sequence of numbers: ')
n = int(input('Enter number: '))
max = 0

while (n!=0):
    if (n>max):
        max = n
    n = int(input('Enter number: '))

print(max)