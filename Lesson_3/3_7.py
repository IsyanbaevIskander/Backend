string = input('Введите строку: ').lower()

# С учетом пробелов
start, end = 0, len(string) - 1
is_palindrom = True
while start <= end:
    if string[start] != string[end]:
        is_palindrom = False
        break
    start += 1
    end -= 1
print('Палиндром' if is_palindrom else 'Не палиндром')

# Без учета пробелов
start, end = 0, len(string) - 1
is_palindrom = True
while start <= end:
    while string[start] == ' ':
        start += 1
    while string[end] == ' ':
        end -= 1
    if string[start] != string[end]:
        is_palindrom = False
        break
    start += 1
    end -= 1
print('Палиндром' if is_palindrom else 'Не палиндром')
