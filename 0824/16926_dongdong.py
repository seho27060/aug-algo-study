# 백준 16926 배열 돌리기 1
# 반시계방향으로 회전시킨다,, R만큼 회전하기

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(R):
    for i in range(min(N, M) // 2):  # 범위는 가로와 세로 중 짧은 길이의 절반
        x, y = i, i # 도는 배열 중 가장 첫번째 인덱스
        tmp = arr[x][y]

        for j in range(i+1, N-i):   # 좌로 회전
            x = j
            p_value = arr[x][y]
            arr[x][y] = tmp
            tmp = p_value

        for j in range(i + 1, M - i):  # 아래로 회전
            y = j
            p_value = arr[x][y]
            arr[x][y] = tmp
            tmp = p_value

        for j in range(i + 1, N - i):  # 우로 회전
            x = N-j-1
            p_value = arr[x][y]
            arr[x][y] = tmp
            tmp = p_value

        for j in range(i + 1, M - i):  # 위로 회전
            y = M-j-1
            p_value = arr[x][y]
            arr[x][y] = tmp
            tmp = p_value

for i in range(N):
    for j in range(M):
        print(arr[i][j], end=" ")
    print()
