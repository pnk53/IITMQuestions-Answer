print('Enter a string: ')
string = str(input())
lower_string = string.lower()
#print(lower_string)
length = len(lower_string)
list = []
for i in range(0, length):
    list.append(lower_string[i])
#print(list)
for i in range(0, length):
    for j in range(0, length):
        if (list[i] < list[j]):
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
sort = ''
for i in range(0,length):
    sort = sort + list[i]
print(sort)


'''sort = ''.join(sorted(lower_string))
print(sort)'''