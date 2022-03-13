print('Enter your email id: ')
email = str(input())

branch = email[0:2]
degree = email[3:5]
year = email[6:8]
roll = email[9:13]

print(branch)
print(degree)
print(year)
print(roll)

# print(branch, degree, year, roll, sep='\n')