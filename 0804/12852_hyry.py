from heapq import heappop, heappush

def bfs():
    Q = [(0, N, [N])]
    visit = [False] * (N + 1)

    while Q:
        cost, curV, lst = heappop(Q)
        if visit[curV]: continue
        if curV == 1: return cost, lst
        visit[curV] = True

        if curV % 3 == 0:
            heappush(Q, (cost + 1, curV // 3, lst[::] + [curV // 3]))
        if curV % 2 == 0:
            heappush(Q, (cost + 1, curV // 2, lst[::] + [curV // 2]))
        if curV - 1 > 0:
            heappush(Q, (cost + 1, curV - 1, lst[::] + [curV - 1]))

    return -1, lst


N = int(input())
ans, ansLst = bfs()
print(ans)
print(*ansLst)