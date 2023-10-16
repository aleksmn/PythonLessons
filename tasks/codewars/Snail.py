
def snail(m):
    n = len(m)
    result = []
    start_x, start_y = 0, 0
    end_x, end_y = n - 1, n - 1

    x = start_x
    while x <= end_x:
        result.append(m[start_y][x])
        x += 1

    y = start_y + 1
    while y <= end_y:
        result.append(m[y][end_x])
        y += 1


    return result




array = [[1,2,3],
         [8,9,4],
         [7,6,5]]

print(snail(array))




