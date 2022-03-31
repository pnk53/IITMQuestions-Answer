print('Enter sequence of words: ')
word = str(input('Enter word: '))
small = word
while (word != 'abcdefghijklmnopqrstuvwxyz'):
    if (len(word) < len(small)):
        small = word
    word = str(input('Enter word: '))
print(small)
