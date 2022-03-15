print('Enter the co-ordinates of point: ')
x = float(input('Enter X-Coordinate: '))
y = float(input('Enter Y-Coordinate: '))

if (x==0 and y==0):
    print('origin')
elif (x==0 and y!=0):
    print('y-axis')
elif (x!=0 and y==0):
    print('x-axis')
elif (x>0 and y>0):
    print('first')
elif (x>0 and y<0):
    print('fourth')
elif (x<0 and y>0):
    print('second')
else:
    print('third')