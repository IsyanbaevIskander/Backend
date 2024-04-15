digits = input('Введите числа через запятую: ')
array_1 = [int(i) for i in digits.split(',')]   # список
array_2 = tuple(array_1)                        # кортеж