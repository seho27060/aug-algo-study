import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a, b = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(n)]
print(maps)
k = n//3
cost = 1e10

def func(sY, sX, num):
    global cost
    if sY+(num*3)>n or sX+(num*3)>m:
        return
    tmp = 0
    for row in range(n):
        for col in range(m):
            # 범위 안일 때
            if sY<=row<sY+(num*3) and sX<=col<sX+(num*3):
                # ㄷ의 빈곳
                if sY+num<=row<sY+num*2 and sX+num<=col:
                    if maps[row][col] == '#':
                        tmp += b
                else:
                    if maps[row][col] == '.':
                        tmp += a
            # 범위 밖 & 검은색
            else:
                if maps[row][col] == '#':
                    tmp += b
    cost = min(cost, tmp)  

level = 0
while level < k:
    level += 1
    for i in range(n):
        for j in range(m):
            func(i, j, level)
print(cost)