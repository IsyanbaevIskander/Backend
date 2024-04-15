arr_1 = [2, 'два', 2.0001, 'two']
arr_2 = [3, 'три', 3.0001, 'three']
# Первый способ
ans_1 = arr_1 + arr_2
print(ans_1)

# Второй способ
arr_1.extend(arr_2)
print(arr_1)