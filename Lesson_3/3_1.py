n = int(input('Введите целое число: '))

summ = 0
# Первый способ
for i in range(2, n + 1, 2):
    summ += i
print(summ)

# Второй способ
summ = 0
curr = 2
while curr <= n:
    summ += curr
    curr += 2
print(summ)