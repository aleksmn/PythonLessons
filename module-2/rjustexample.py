
my_dictionary = {
    'один': 'one',
    'два': 'two',
    'три': 'three'
}


print('-'*42)

for k, v in my_dictionary.items():
    output = f'{k} : {v}'

    print(f"|{output.ljust(40, ' ')}|")

    # print(f'|{k.ljust(20)}{v.just(20)}|')

print('-'*42)
