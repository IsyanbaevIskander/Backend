string = input()
counter = 0
is_word = False
for i in string:
    if i.isalnum():
        if not is_word:
            counter += 1
            is_word = True
    else:
        is_word = False
print(counter)