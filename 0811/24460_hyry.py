
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def selectFour(x1, x2, y1, y2):
    if x2 - x1 <= 1 and y2 - y1 <= 1:
        return arr[x1][y1]

    a = selectFour(x1, (x1 + x2) // 2, y1, (y1 + y2) // 2)
    b = selectFour(x1, (x1 + x2) // 2, (y1 + y2) // 2, y2)
    c = selectFour((x1 + x2) // 2, x2, y1, (y1 + y2) // 2)
    d = selectFour((x1 + x2) // 2, x2, (y1 + y2) // 2, y2)

    minV = minV2 = 1e10
    for num in (a, b, c, d):
        if minV > num:
            minV2 = minV
            minV = num
        elif minV < num < minV2:
            minV2 = num

    return minV2


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(selectFour(0, N, 0, N))
