def is_sublist(larger, smaller):
    n = len(larger)
    m = len(smaller)
    
    if m > n:
        return False
    
    for i in range(n - m + 1):
        if larger[i:i+m] == smaller:
            return True
        
    return False




list_1= [4, 8, 1, 0, 12,  6]
list_2= [1, 0, 12]


print(is_sublist(list_1, list_2))