n, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
v = [0] * n
sol = 1e9
def dfs(s, m, c):
    global sol

    if s == n:

        sol = min(sol, c)
        return
    for i in range(n):
        if v[i] == 0:
            v[i] = 1
            dfs(s+1, i, c+arr[m][i])
            v[i] = 0


v[k] = 1
for m in range(n):
    for a in range(n):
        for b in range(n):
            arr[a][b] = min(arr[a][b], arr[a][m]+arr[m][b])



dfs(1,k,0)
print(sol)