print('Enter a number: ')
x = float(input())

if (0<x<10):
    funx = x+2
elif (x>=10):
    funx = (x**2) + 2
else:
    funx = 0

print(funx)