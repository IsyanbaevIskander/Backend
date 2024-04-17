from random import randint

n = int(input('Введите размер массива: '))
arr = [randint(1, 100) for i in range(n)]
arr.sort()
print(arr)  # для наглядности
copy = [i for i in arr]
# Первый способ
index = 0
while index < len(arr):
    while arr.count(arr[index]) > 1:
        arr.pop(index)
    index += 1
print(arr)

# Второй способ
for i in copy:
    if copy.count(i) > 1:
        copy.remove(i)
print(copy)