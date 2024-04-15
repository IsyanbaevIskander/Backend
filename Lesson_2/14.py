from random import randint

n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
array = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        array[i][j] = randint(0, 100)
for i in array:
    print(*i)
print()

answer = [[0] * n for i in range(m)]
for i in range(m):
    for j in range(n):
        answer[i][j] = array[j][i]
for i in answer:
    print(*i)