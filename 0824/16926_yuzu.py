N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def rotate(N, M, R, arr):
    k = min(N, M)//2
    for _ in range(R):
        num = 0
        for _ in range(k):
            num1 = arr[num][num]
            for i in range(1+num, M-num):
                arr[num][i-1] = arr[num][i]
            for i in range(num, N-1-num):
                arr[i][M-1-num] = arr[i+1][M-1-num]
            for i in range(M-1-num, 0+num, -1):
                arr[N-1-num][i] = arr[N-1-num][i-1]
            for i in range(N-1-num, 0+num, -1):
                arr[i][num] = arr[i-1][num]
            arr[num+1][num] = num1
            num += 1
    return arr

ans = rotate(N, M, R, arr)
for i in range(N):
    print(*ans[i])