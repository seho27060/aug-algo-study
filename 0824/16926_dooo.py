n, m, r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

for _ in range(r):
    ans = [[0] * m for _ in range(n)]
    for i in range(min(n,m)//2):
        for k in range(i+1, n-i):
            ans[k][i] = arr[k-1][i]
        for j in range(i+1, m-i):
            ans[n-1-i][j] = arr[n-1-i][j-1]
        for t in range(n-2-i,-1+i, -1):
            ans[t][m-1-i] = arr[t+1][m-1-i]
        for l in range(m-2-i,-1+i,-1):
            ans[i][l] = arr[i][l+1]
    arr = ans
for i in ans:
    print(*i)