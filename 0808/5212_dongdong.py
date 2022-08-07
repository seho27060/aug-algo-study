# 백준 5212 지구온난화
import copy

R, C = map(int, input().split())
arr = [list(input())for _ in range(R)]
result = copy.deepcopy(arr) # 결과 지도를 위한 배열 복사, 2차원 배열부터는 deepcopy를 해야한다!!


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for x in range(R):
    for y in range(C):
        cnt = 0     # 바다인 면의 개수를 세자
        if arr[x][y] == '.':    # 바다인 경우 그냥 넘어감 탐색할 필요x
            continue

        for i in range(4):   # 상하좌우 돌거임
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C: # 범위 체크
                if arr[nx][ny] == '.':  # if 바다면
                    cnt += 1
            else:   # 조건에 범위 바깥의 공간은 전부 바다라고 주어짐!! 즉, 범위가 벗어난다면 바다
                cnt += 1

        if cnt >= 3:    # 바다가 접하는 면이 3이상이면
            result[x][y] = '.'      # 결과 배열을 .으로 바꿔준다

# print(result)
# 어떻게 잘라서 print해야 할까.......

row = []
column = []

for i in range(R):
    for j in range(C):
        if result[i][j] == 'X':     # X 위치 찾기
            row.append(i)
            column.append(j)

# print(row)
# print(column)

row_s = min(row)
row_e = max(row)
col_s = min(column)
col_e = max(column)

for i in range(row_s, row_e+1):
    for j in range(col_s, col_e+1):
        print(result[i][j], end="")
    print()
