print('Enter the sequence: ')
x=0
y=0
seq = str(input('Enter command: ')).lower()
while (seq != 'end'):
    seq = str(input('Enter Command: ')).lower()
    if(seq == 'start'):
        x=0
        y=0
    elif(seq == 'up'):
        x=x+0
        y=y+1
    elif(seq == 'down'):
        x=x+0
        y=y-1
    elif(seq == 'right'):
        x=x+1
        y=y+0
    elif(seq == 'left'):
        x=x-1
        y=y+0

dist = abs(x) + abs(y)
print(dist)