import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    # a = 작은 애 / b = 큰 애
    a, b = map(int, input().split())
    arr[a][b] = -1
    arr[b][a] = +1

for num in range(1, N+1):
    for row in range(1, N+1):
        for col in range(1, N+1):
            if row == col:
                continue
            if arr[row][num] and arr[num][col]:
                if arr[row][num] == arr[num][col]:
                    if arr[row][num] == 1:
                        arr[row][col] = 1
                        arr[col][row] = -1
                    else:
                        arr[row][col] = -1
                        arr[col][row] = 1

cnt = 0
for _ in range(1, N+1):
    if arr[_][1:].count(0) == 1:
        cnt += 1
    print(arr[_])

print(cnt)