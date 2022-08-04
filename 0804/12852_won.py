import sys
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

N = int(input())

def f(n):
    qu = deque()
    visited = [0] * (10 ** 6 + 1)
    qu.append([n, [n]])
    visited[n] = 1
    while qu:
        cur, cur_list = qu.popleft()

        if cur == 1:
            return visited[cur] - 1, cur_list

        if visited[cur // 3] == 0 and cur % 3 == 0:
            qu.append([cur // 3, cur_list + [cur // 3]])
            visited[cur // 3] = visited[cur] + 1

        if visited[cur // 2] == 0 and cur % 2 == 0:
            qu.append([cur // 2, cur_list + [cur // 2]])
            visited[cur // 2] = visited[cur] + 1

        if visited[cur - 1] == 0 and cur - 1 >= 1:
            qu.append([cur - 1, cur_list + [cur - 1]])
            visited[cur - 1] = visited[cur] + 1

ans, lst = f(N)

print(ans)
print(*lst)
