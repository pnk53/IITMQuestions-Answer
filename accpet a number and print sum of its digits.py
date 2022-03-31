print('Enter a number: ')
n = int(input())

rem = n % 10
n = n // 10
sum = rem
while (n !=0):
    r = n % 10
    n = n // 10
    sum = sum + r
print(sum)

'''n1 = str(n)
sum = 0
for i in n1:
    sum = sum + int(i)
print(sum)'''