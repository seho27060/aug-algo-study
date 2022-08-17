import sys
input = sys.stdin.readline
# from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations


N = int(input())
arr = list(map(int, input().split()))
arr.sort()

minV = 20000000001
l = 0
r = N - 1
while l < r:
    sumV = arr[l] + arr[r]

    if minV > abs(sumV):
        minV = abs(sumV)
        ans = [arr[l], arr[r]]

    if sumV == 0:
        break
    if sumV > 0:
        r -= 1
    if sumV < 0:
        l += 1

print(*ans)
