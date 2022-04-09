print('Enter a value: ')
n = int(input())

for i in range(1,n+2):
    for j in range(1,i):
        print(j, end='')
    print('')
for i in range(n,0,-1):
    for j in range(1,i):
        print(j, end='')
    print('')