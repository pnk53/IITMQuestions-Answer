print('Enter a number: ')
n = int(input())
sum = 0
prime = True
list = []
for i in range (2,n+1):
    for j in range (2, i):
        if (i%j == 0):
            prime = False
    if (prime):
        sum = sum + i
    prime = True
print(sum)