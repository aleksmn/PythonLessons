output = ''

with open('names.txt', 'r', encoding='utf-8') as f:
    for line in f:
        a, b, c = line.split()
        short_name = f'{a} {b[0]}.{c[0]}.\n'
        output = output + short_name
        # print(short_name)

with open('initials.txt', 'a', encoding='utf-8') as f:
    f.write(output)
