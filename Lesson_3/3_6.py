n = int(input('Введите число: '))

# Первый способ
count = 0
for i in str(n):
    count += 1
print(count)

# Второй способ
count = 0
while count < len(str(n)):
    count += 1
print(count)

# Третий способ ('_')
print(len(str(n)))