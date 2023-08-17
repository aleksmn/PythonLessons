import timeit


nums = [-22, -3, -1, -9, -12, -19, -10]


def flawed(a: list):
    largest = 0
    for n in a:
        if largest < n:
            largest = n
    return largest

def get_largest(a: list):
    largest = a[0]
    for i in range(1, len(a)):
        if largest < a[i]:
            largest = a[i]
    return largest

def get_largest_2(a: list):
    largest = None
    for i in a:
        if largest is None or largest < i:
            largest = i
    return largest


reps = 1000000

print('flawed:', timeit.timeit(lambda: flawed(nums), number=reps))
print('get_largest:', timeit.timeit(lambda: get_largest(nums), number=reps))
print('get_largest_2:', timeit.timeit(lambda: get_largest_2(nums), number=reps))


