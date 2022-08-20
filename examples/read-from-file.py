# with open('names.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         a, b, c = line.split()
#         print(f'{a} {b[0]}.{c[0]}.\n')


with open('names.txt', 'r', encoding='utf-8') as f:
    for line in f:
        a, b, c = line.split()
        short_name = f'{a} {b[0]}.{c[0]}.\n'
        # print(short_name)
        with open('initials.txt', 'a', encoding='utf-8') as f:
            f.write(short_name)
