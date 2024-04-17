from random import randint

n = int(input('Введите размер массива: '))
arr = [randint(1, 10000) for i in range(n)]
# Без циклов
if len(arr) != len(set(arr)):
    print('Есть дубликаты')
else:
    print('Все элементы уникальны')

# С циклами
buffer = []
is_unique = True
for i in arr:
    if i in buffer:
        is_unique = False
        break
    buffer.append(i)
print('Все элементы уникальны' if is_unique else 'Есть дуюликаты')