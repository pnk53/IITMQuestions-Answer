print('Enter a starting position: ')
start = input()
print('Enter a ending position: ')
end = input()

s = 'ABCDEFGH'

if (abs(s.index(start[0]) - s.index(end[0])) == abs(int(start[1]) - int(end[1]))):
    print('Yes')
else:
    print('No')
