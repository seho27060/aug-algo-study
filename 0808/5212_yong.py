# 규칙에 맞춰 구현하는 문제
# 첫 탐색 시 인접한 면이 3 이상은 육지는 리스트에 저장
# 3 미만인 육지는 최대 최소 좌표 갱신
# 잠길 육지를 바꾼 후 최대 최소 좌표를 기반으로 답을 출력

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

R, C = map(int, input().split())
check = [[0] * C for _ in range(R)]
arr = [list(input()) for _ in range(R)]
change = []
maxY = maxX = -1
minY = minX = 11

for y in range(R):
    for x in range(C):
        if arr[y][x] == 'X':
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < R and 0 <= nx < C:
                    if arr[ny][nx] == '.':
                        check[y][x] += 1
                else:
                    check[y][x] += 1
            if check[y][x] >= 3:
                change.append((y, x))
            else:
                if minY > y:
                    minY = y
                if maxY < y:
                    maxY = y
                if minX > x:
                    minX = x
                if maxX < x:
                    maxX = x
                    
for y, x in change:
    arr[y][x] = '.'
if maxY == minY and minX == maxX:
    print("X")
else:
    for i in range(minY, maxY+1):
        for j in range(minX, maxX+1):
            print(arr[i][j], end='')
        print()