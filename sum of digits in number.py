print('Enter a number: ')
n = int(input())
rem = n % 10
n = n // 10

while (n>0):
    r = n % 10
    n = n // 10
    rem = rem + r

print(rem)

