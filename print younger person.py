print('Enter name and birthdate of 2 person: ')
name1 = str(input('Enter name of 1st Person: ')).lower()
date1 = str(input('Enter birthdate: '))
name2 = str(input('Enter name of 2nd Person: ')).lower()
date2 = str(input('Enter birthdate: '))
list = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
        'x', 'y', 'z']
#Exact same birthdate: Look for alphabets
if (date1 == date2):
    if (list.index(name1[0]) < list.index(name2[0])):
        print(f'{name2} is younger.')
    else:
        print(f'{name1} is younger.')

else:
    if (int(date1[6:10]) < int(date2[6:10])):                     #When there's difference in year.
        print(f'{name2} is younger.')
    elif(int(date1[6:10]) > int(date2[6:10])):
        print(f'{name1} is younger.')
    else:
       if (int(date1[3:5]) < int(date2[3:5])):                    #When year are same and there's difference in months
           print(f'{name2} is younger.')
       elif (int(date1[3:5]) > int(date2[3:5])):
           print(f'{name1} is younger.')

       else:
           if (int(date1[0:2]) < int(date2[0:2])):                #When year and month are same and there's difference in date.
               print(f'{name2} is younger.')
           else:
               print(f'{name1} is younger.')

