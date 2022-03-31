print('Enter 2 number: ')
a = int(input('Enter a: '))
b = int(input('Enter b: '))
sum = 0
for i in range (1000, 2001):
    if (i%a==0 and i%b==0):
        sum = sum + i
print(sum)

