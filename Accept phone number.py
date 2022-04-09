print('Enter your phone number: ')
n = input()
a = False
if (n.isdigit() and len(n) == 10 and int(n[0]) > 5):
    for i in range(10):
        if (n.count(n[i])<8):
            a = True
            if (n[i]*6 in n):
                a = False
                break
        else:
            break
if(a):
    print('Valid')
else:
    print('Invalid')

