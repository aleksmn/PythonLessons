def linear_search(list, target):
    """
    Возвращает позицию значения target,
    возвращает None, если такого значения нет.
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


print(linear_search([3, 1, 0, 9], 0))