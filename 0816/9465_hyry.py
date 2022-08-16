
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    if N > 1:
        arr[0][1] = max(arr[0][0], arr[1][0] + arr[0][1])
        arr[1][1] = max(arr[1][0], arr[0][0] + arr[1][1])

    for col in range(2, N):
        arr[0][col] = max(arr[1][col - 1], arr[1][col - 2]) + arr[0][col]
        arr[1][col] = max(arr[0][col - 1], arr[0][col - 2]) + arr[1][col]

    print(max(arr[0][N - 1], arr[1][N - 1]))
