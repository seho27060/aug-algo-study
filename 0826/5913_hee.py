D = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def func(x, y, apples):
    if x == 4 and y == 4 and apples == 0:
        global ans
        ans += 1
        return

    for dx, dy in D:
        nx = x + dx
        ny = y + dy
        if -1 < nx < 5 and -1 < ny < 5 and G[ny][nx]:
            G[ny][nx] = 0
            func(nx, ny, apples - 1)
            G[ny][nx] = 1
            
K = int(input())

G = [[1] * 5 for _ in range(5)]
G[0][0] = 0
for _ in range(K):
    A, B = map(int, input().split())
    G[A-1][B-1] = 0
    
ans, total = 0, 5 * 5 - K -1
func(0, 0, total)
print(ans)