print('Пн Вт Ср Чт Пт Сб Вс')
for i in range(1, 32):
    if i < 10:
        print(f' {i}', end=' ')
    else:
        print(i, end=' ')

    if i % 7 == 0:
        print()