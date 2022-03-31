print('Enter a number: ')
n = int(input())
prime = True
if(n>1):
    for i in range (2,n):
        if (n%i == 0):
            prime = False

    if (prime):
        print('Prime')
    else:
        print('Not prime')
else:
    print('Invalid Input')