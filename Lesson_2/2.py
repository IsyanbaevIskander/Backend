string = input()
if string.count('h') >= 2:
    a, b = string.find('h'), string.rfind('h')
    string = string[:a + 1] + string[a + 1:b].replace('h', 'H') + string[b:]
print(string)
