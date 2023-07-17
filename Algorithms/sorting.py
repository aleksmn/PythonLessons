def bubble_sort(arr):
    n = len(arr)
    # Повторяем проходы по массиву, пока не будет выполнено условие сортировки
    for i in range(n-1):
        # Установка флага, указывающего, были ли сделаны обмены на текущей итерации
        swapped = False
        # Сравнение и обмен каждой пары соседних элементов
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # Если обмены не были выполнены на текущей итерации, массив уже отсортирован
        if not swapped:
            break
    return arr

# Пример использования
array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = bubble_sort(array)
print(sorted_array)





def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Разбиваем массив на две половины
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Рекурсивно применяем сортировку слиянием к каждой половине
        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)
        
        # Слияние отсортированных половин в один массив
        merged = merge(left_half, right_half)
        
        return merged

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    # Сравниваем элементы и добавляем их в новый массив в правильном порядке
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Копируем оставшиеся элементы из одной из половин
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    
    return merged

# Пример использования
array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = merge_sort(array)
print(sorted_array)



def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Выбор опорного элемента
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        # Рекурсивное применение быстрой сортировки к обоим подмассивам
        return quicksort(less) + [pivot] + quicksort(greater)

# Пример использования
array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = quicksort(array)
print(sorted_array)