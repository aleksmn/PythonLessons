text_string = input('Текст: ').lower()
text = text_string.split(' ')

for i in range(len(text)):
    # 1 способ
    punctuation = ',.!?:;'
    for sign in punctuation:
        text[i] = text[i].replace(sign, '')

words = {}
for word in text:
    num = 1
    if word in words:
        words[word] = words[word] + 1
    else:
        words[word] = num


for key in words:
    print(f'{key} - {words[key]}')
