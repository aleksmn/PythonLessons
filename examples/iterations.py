import itertools



alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Комбинации с повторами
combinations = itertools.permutations(alphabet, 2)


# Комбинации без повторов
# combinations = itertools.combinations(alphabet, 2)


# combinations = itertools.product(alphabet, repeat=2)

count = 0
for combination in combinations:
    print(''.join(combination), end=" ")
    count += 1
    if count % 20 == 0:
        print()

print("\nCount:", count)


# ab ac ad ae af ag ah ai aj ak al am an ao ap aq ar as at au av aw ax ay az
# ab ac ad ae af ag ah ai aj ak al am an ao ap aq ar as at au av aw ax ay az 




'''

Модули itertools.product, itertools.combinations и itertools.permutations предлагают различные способы генерации комбинаций элементов. Вот объяснение разницы между ними:

itertools.product: Эта функция генерирует декартово произведение заданных итерируемых объектов. Она создает все возможные комбинации элементов из каждого итерируемого объекта. Например, если у вас есть два итерируемых объекта A = [1, 2] и B = ['a', 'b'], то product(A, B) создаст комбинации (1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'). Функция product может принимать несколько итерируемых объектов и имеет параметр repeat, который задает длину комбинаций.

itertools.combinations: Эта функция генерирует все возможные комбинации заданной длины из итерируемого объекта. Например, если у вас есть итерируемый объект A = [1, 2, 3], то combinations(A, 2) создаст комбинации (1, 2), (1, 3), (2, 3). Функция combinations не учитывает порядок элементов и не повторяет элементы в комбинациях.

itertools.permutations: Эта функция генерирует все возможные перестановки заданной длины из итерируемого объекта. Например, если у вас есть итерируемый объект A = [1, 2, 3], то permutations(A, 2) создаст перестановки (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2). Функция permutations учитывает порядок элементов и не повторяет элементы в перестановках.

Таким образом, основная разница между product, combinations и permutations заключается в том, как они генерируют комбинации элементов: product создает все комбинации элементов из нескольких итерируемых объектов, combinations создает комбинации заданной длины без повторения элементов, а permutations создает перестановки заданной длины без повторения элементов.



'''