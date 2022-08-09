
def bfs():
    Q = [(0, 0)]
    visit = [False] * N
    visit[0] = True

    while Q:
        cost, curV = Q.pop(0)
        if curV == N - 1:
            return cost

        for neiV in range(curV + 1, curV + arr[curV] + 1):
            if neiV <= N - 1 and not visit[neiV]:
                Q.append((cost + 1, neiV))
                visit[neiV] = True

    return -1


N = int(input())
arr = list(map(int, input().split()))

print(bfs())

