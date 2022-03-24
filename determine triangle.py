print('Enter side a: ')
a = int(input())
print('Enter side b: ')
b = int(input())
print('Enter side c: ')
c = int(input())

if(a+b>c and b+c>a and c+a>b):
    print('Yes')
else:
    print('No')
