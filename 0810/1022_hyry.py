def spiral(row, col):
    x = max(abs(row), abs(col))
    tmp = (x * 2 - 1) ** 2 + 1
    cnt = ((x * 2 + 1) ** 2 - tmp + 1) // 4

    if row == col == x:
        return (x * 2 + 1) ** 2

    if row == x:
        idx = x + col - 1
        return tmp + cnt * 3 + idx

    elif row == -x:
        idx = x - col - 1
        return tmp + cnt + idx

    elif col == x:
        idx = x - row - 1
        return tmp + idx

    elif col == -x:
        idx = x + row - 1
        return tmp + cnt * 2 + idx


r1, c1, r2, c2 = map(int, input().split())

arr = []
maxV = 0
for row in range(r1, r2 + 1):
    for col in range(c1, c2 + 1):
        val = spiral(row, col)
        arr.append(val)
        maxV = max(maxV, val)

length = len(str(maxV))
numCnt = 0
for num in arr:
    print(' ' * (length - len(str(num))) + str(num), end=" ")
    numCnt += 1
    if numCnt % (c2 - c1 + 1) == 0:
        print()