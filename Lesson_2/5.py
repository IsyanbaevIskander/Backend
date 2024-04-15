string = input('Введите два слова через пробел: ')
string = string.split()
string = ' '.join(string[::-1])
print(string)