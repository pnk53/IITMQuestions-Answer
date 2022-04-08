print('Enter a positive integer: ')
n = int(input())
for f in range (2,n+1):
    if n%f == 0:
        prime = True
        #print(f)
        for i in range (2,f):
            if f%i == 0:
                prime = False
                break
        if (prime):
            print(f)