def findRoute(row, col):
    global cnt

    if row == col == 4:
        if len(visit) == 25 - K:
            cnt += 1
        return

    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        newR, newC = row + dr, col + dc
        if 0 <= newR < 5 and 0 <= newC < 5 and \
                (newR, newC) not in visit and MAP[newR][newC]:
            visit.add((newR, newC))
            findRoute(newR, newC)
            visit.remove((newR, newC))


MAP = [[1] * 5 for _ in range(5)]
visit = {(0, 0)}
cnt = 0

K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    MAP[i - 1][j - 1] = 0

findRoute(0, 0)

print(cnt)
