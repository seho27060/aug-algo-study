import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
# from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

N = int(input())

G = [list(map(int, input().split())) for _ in range(N)]

def f(r2, r1, c2, c1):
    if r2 - r1 == 1 and c2 - c1 == 1:
        return G[r1][c1]

    res1 = f((r2 + r1) // 2, r1, (c2 + c1) // 2, c1)
    res2 = f(r2, (r2 + r1) // 2, (c2 + c1) // 2, c1)
    res3 = f((r2 + r1) // 2, r1, c2, (c2 + c1) // 2)
    res4 = f(r2, (r2 + r1) // 2, c2, (c2 + c1) // 2)

    # print(res1, res2, res3, res4)

    fst = 2 ** 31
    sec = 2 ** 31

    for res in [res1, res2, res3, res4]:
        if fst > res:
            sec = fst
            fst = res
        elif sec > res > fst:
            sec = res

    return sec


ans = f(N, 0, N, 0)

print(ans)
