print('Enter two numbers M and N: ')
m = int(input())
n = int(input())

if(m<n):
    print(m)
else:
    m1=m-n       # print (m%n) whole else condition can be written like this.
    while(m1 >= n):
        m1=m1-n
    print(m1)
