import sys
input = sys.stdin.readline
from collections import deque
# from heapq import heappush, heappop
# from collections import defaultdict
# from itertools import permutations

N = int(input())

if N == 1:
    print(0)
    exit()

arr = list(map(int, input().split()))
# print(arr)

def f():
   qu = deque()
   visited = [0] * N
   qu.append(0)
   visited[0] = 1
   while qu:
       t = qu.popleft()

       for i in range(t + 1, t + arr[t] + 1):
           if i == N - 1:
               return visited[t]
           if i < N - 1 and visited[i] == 0:
               qu.append(i)
               visited[i] = visited[t] + 1
   return -1

ans = f()
print(ans)
