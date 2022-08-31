# 브포 알고리즘
# 왜 아직도 or랑 and 조건 활용을 제대로 못하겠지...?

def find(k, y, x):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if (y <= i < y+k or y+k*2 <= i < y+k*3) and x <= j < x+k*3:
                if arr[i][j] == '.':
                    cnt += a
            elif y <= i < y+k*3 and x <= j < x+k:
                if arr[i][j] == '.':
                    cnt +=a
            else:
                if arr[i][j] == '#':
                    cnt += b
    return cnt



n, m = map(int, input().split())
a, b = map(int, input().split())

arr = [list(input()) for _ in range(n)]

k = min(n, m) // 3
ans = 10000000000000000
for i in range(1, k+1):
    for j in range(n-i*3+1):
        for l in range(m-i*3+1):
            val = find(i, j, l)
            if val < ans:
                ans = val
print(ans)