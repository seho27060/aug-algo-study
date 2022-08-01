R, C = map(int, input().split())
heights = list(map(int, input().split()))

blocks = [[1] * C for _ in range(R)]

for col in range(C):
    for row in range(0, R - heights[col]):
        blocks[row][col] = 0

ans = 0
for row in range(R):
    flag = False
    cnt = 0
    for col in range(C):
        if flag:
            cnt += 1
        if blocks[row][col]:
            flag = True
            if cnt: ans += cnt - 1
            cnt = 0

print(ans)