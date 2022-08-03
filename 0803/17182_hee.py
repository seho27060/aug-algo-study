# 다익스트라 풀이
# from heapq import *
# import sys
# INF = sys.maxsize
# input = sys.stdin.readline
#
# def dijk():
#     for i in range(N):
#         D[i][i] = 0
#         Q = [(0, i)]
#         while Q:
#             c, n1 = heappop(Q)
#
#             if D[i][n1] < c:
#                 continue
#
#             for n2, cost in enumerate(G[n1]):
#                 if cost + c < D[i][n2]:
#                     D[i][n2] = cost + c
#                     heappush(Q, (D[i][n2], n2))
#
# def func(idx, node, sum_val):
#     if idx == N:
#         global ans
#         ans = min(ans, sum_val)
#         return ans
#
#     for i in range(N):
#         if not V[i]:
#             V[i] = True
#             func(idx+1, i, sum_val + D[node][i])
#             V[i] = False
#
# G = []
# N, K = map(int, input().split())
# for _ in range(N):
#     G.append(list(map(int, input().split())))
#
# D = [[INF] * N for _ in range(N)]
# V = [False] * N
# ans = INF
# dijk()
# func(0, K, 0)
# print(ans)

# 플로이드 워샬 풀이
import sys
INF = sys.maxsize

def func(idx, node, sum_val):
    global ans
    if idx == N:
        ans = min(ans, sum_val)
        return ans

    if ans < sum_val:
        return

    for i in range(N):
        if not V[i]:
            V[i] = True
            func(idx+1, i, sum_val + D[node][i])
            V[i] = False

D = []
N, K = map(int, input().split())
for _ in range(N):
    D.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        for k in range(N):
            D[j][k] = min(D[j][k], D[j][i] + D[i][k])

V = [False] * N
ans = INF
func(0, K, 0)
print(ans)