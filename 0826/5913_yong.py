# 브포, 백트래킹
# 재귀를 활용해 풀었음!

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
def find(y, x, a):
    global ans
    if y == 5 and x == 5 and a == 0:
        ans += 1
        return
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 1 <= ny <= 5 and 1 <= nx <= 5 and not arr[ny][nx]:
            arr[ny][nx] = 1
            find(ny, nx, a-1)
            arr[ny][nx] = 0


K = int(input())
arr = [[0] * 6 for _ in range(6)]
for _ in range(K):
    y, x = map(int, input().split())
    arr[y][x] = 1
arr[1][1] = 1
ans = 0
cnt = 24 - K
find(1, 1, cnt)
print(ans)