print('Enter a integer: ')
n = int(input())
c = True
for x in range (1,n):
    for y in range (1,n):
        for z in range (1,n):
            if ((x**2 + y**2 == z**2) and x<y<z<n):
                print(x,y,z, sep=',')
                c = False
if(c):
    print('No solution')