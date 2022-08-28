import sys
from heapq import heappop, heappush
input = sys.stdin.readline


def findPrincess():
    Q = [(0, 0, 0, False)]
    visit = set()

    while Q:
        curT, curR, curC, sword = heappop(Q)
        if (curR, curC, sword) in visit: continue
        if curT > T: return "Fail"
        if (curR, curC) == (R - 1, C - 1): return curT
        visit.add((curR, curC, sword))

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            newR, newC = curR + dr, curC + dc
            if 0 <= newR < R and 0 <= newC < C:
                if sword and (newR, newC, sword) not in visit:
                    heappush(Q, (curT + 1, newR, newC, sword))
                if not sword and MAP[newR][newC] != 1 and (newR, newC, MAP[newR][newC] == 2) not in visit:
                    heappush(Q, (curT + 1, newR, newC, MAP[newR][newC] == 2))

    return "Fail"


R, C, T = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]

print(findPrincess())
