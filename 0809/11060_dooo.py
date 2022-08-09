import heapq

N = int(input())
lst = list(map(int, input().split()))
v = [0] * N

def bfs(s):
    q = []
    q.append((s, lst[s]))
    v[s] = 1
    while q:
        cidx, cjump = q.pop(0)
        for i in range(1, cjump +1):
            if  cidx+i < N and v[cidx+i]==0:
                v[cidx+i] = v[cidx] + 1
                q.append((cidx+i, lst[cidx+i]))

bfs(0)
if v[-1] == 0:
    print(-1)
else:
    print(v[-1]-1)
