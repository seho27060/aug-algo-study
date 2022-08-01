import sys
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

H, W = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
for i in range(1, W - 1):
    lm = max(arr[:i])
    rm = max(arr[i + 1:])
    standard = min(lm, rm)
    if standard > arr[i]:
        ans += standard - arr[i]

print(ans)
