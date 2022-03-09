print('Enter a word: ')
word = str(input())
space = ' '
sent = word

while (word != '.'):
    print('Enter a word: ')
    word = str(input())
    sent = sent + space + word

print(sent, end='')

