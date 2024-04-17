from random import randint

n = randint(3, 100)
arr = [randint(1, 1_000_000) for i in range(n)]
for index, digit in enumerate(arr):
    if index % 3 == 2:
        print(f'{index + 1}: {digit}')