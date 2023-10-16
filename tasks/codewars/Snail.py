
def snail(m):
    n = len(m)
    result = []
    x, y = 0, 0
    

    while x < n and y < n:
        # print first row
        for i in range(y, n):
            result.append(m[x][i])
        x += 1

        # print last column
        for i in range(x, n):
            result.append(m[i][n-1])

        n -= 1

        print(x, y)

        if y < n:
            for i in range(n-1, x-1, -1):
                result.append(m[n-1][i])

            n -= 1



    return result




array = [[1,2,3],
         [8,9,4],
         [7,6,5]]

print(snail(array))




