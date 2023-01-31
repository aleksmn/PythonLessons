
my_dictionary = {
    'один': 'one',
    'два': 'two',
    'три': 'three'
}


print('-'*42)

for k, v in my_dictionary.items():
    output = f'{k} : {v}'

    print(f"|{output.rjust(40, ' ')}|")

print('-'*42)
