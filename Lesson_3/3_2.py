n = int(input('Введите количество слов: '))
words = []
for i in range(n):
    curr_word = input('Введите слово: ')
    words.append(curr_word)

# Первый способ
longest = ''
for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)

# Второй способ
longest = ''
i = 0
while i < len(words):
    if len(words[i]) > len(longest):
        longest = words[i]
    i += 1
print(longest)