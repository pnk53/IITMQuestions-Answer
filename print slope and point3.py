print('Enter Coordinates of 2 points: ')
x1 = float(input('x1'))
y1 = float(input('y1'))
x2 = float(input('x2'))
y2 = float(input('y2'))
x3 = float(input('x3'))
print(f'Point1 is ({x1}, {y1}) and Point2 is ({x2}, {y2})')

slope = (y2-y1)/(x2-x1)
print(f'Slope is {slope}')

y3 = y1 + slope*(x3-x1)
print(f'Point3 is ({x3}, {y3})')

if (x1==x2):
    print('Vertical line')
elif (slope>0):
    print('Positive slope')
elif (slope<0):
    print('Negative slope')
else:
    print('Horizontal line')

