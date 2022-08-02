w, h = map(int, input().split())
lst = list(map(int, input().split()))
graph = [[0]*h for _ in range(w)]

for i in range(h):
    k = lst[i]
    while -k < 0:
        graph[-k][i] = 1
        k -= 1

ans = 0
for i in range(w):
    start = 0
    end = 0
    tmp = 0
    for j in range(h):
        if graph[i][j] == 1 and start == 0:
            start = 1
            end = 0
        elif start == 1 and graph[i][j] == 0:
            tmp += 1
        elif start == 1 and graph[i][j] == 1:
            start = 0
            end = 1

        if end == 1:
            ans += tmp

        if graph[i][j] == 1 and start == 0:
            start = 1
            end = 0
            tmp = 0

print(ans)