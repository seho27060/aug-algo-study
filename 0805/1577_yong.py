# DP를 활용한 최단거리 구하기
# 공사 정보가 중복으로 주어지는 경우가 발생하니 이차원 배열을 활용해 저장하자

N, M = map(int, input().split())
K = int(input())
# 공사중인 지점을 저장하기 위한 배열
arr = [[[0] * (N+1) for _ in range(M+1)] for _ in range(2)]
DP = [[0] * (N+1)  for _ in range(M+1)]
DP[0][0] = 1

# a, b, c, d를 받아 두 값을 비교해 공사중인 지점과 방향에 맞는 2차원 배열에 저장 (1 : 행, 2 : 열, 3 : 행과 열)
for _ in range(K):
    a, b, c, d = map(int, input().split())
    if a > c:
        arr[0][b][a] = 1
    if c > a:
        arr[0][d][c] = 1
    if b > d:
        arr[1][b][a] = 2
    if d > b:
        arr[1][d][c] = 2

# 첫행과 첫 열의 DP작업을 우선 진행
for i in range(1, N+1):
    if arr[0][0][i]:
        break
    DP[0][i] = 1
for i in range(1, M+1):
    if arr[1][i][0]:
        break
    DP[i][0] = 1

# arr에 존재하는 값을 기반으로 해당 지점의 DP값을 갱신
for i in range(1, M+1):
    for j in range(1, N+1):
        row = col = 0
        if arr[0][i][j] == 0:
            row = DP[i][j-1]
        if arr[1][i][j] == 0:
            col = DP[i-1][j]
        DP[i][j] = row + col
        
print(DP[M][N])