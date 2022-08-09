
R, C = map(int, input().split())
MAP = [list(input()) for _ in range(R)]

islands = set()

for row in range(R):
    for col in range(C):
        if MAP[row][col] == 'X':
            islands.add((row, col))

for _ in range(50):
    tmp = islands.copy()
    for row, col in islands:
        cnt = 0
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            newR, newC = row + dr, col + dc
            if 0 <= newR < R and 0 <= newC < C:
                if MAP[newR][newC] == '.':
                    cnt += 1
            else:
                cnt += 1
        if cnt >= 3:
            # delete islands
            tmp.remove((row, col))
    if len(tmp) == 0:
        # 이전 섬 개수로
        break
    if len(tmp) == 1:
        islands = tmp
        break
    islands = tmp

rowflag = True
while rowflag:
    rowTmp = set()
    for r, c in islands:
        if not rowflag: break
        if r - 1 >= 0:
            rowTmp.add((r - 1, c))
        else:
            rowflag = False
            break
    else:
        islands = rowTmp

colFlag = True
while colFlag:
    colTmp = set()
    for r, c in islands:
        if not colFlag: break
        if c - 1 >= 0:
            colTmp.add((r, c -1))
        else:
            colFlag = False
            break
    else:
        islands = colTmp

tmpR = tmpC = -1
for r, c in islands:
    tmpR = max(r, tmpR)
    tmpC = max(c, tmpC)

newMAP = [['.'] * (tmpC + 1) for _ in range(tmpR + 1)]

for r, c in islands:
    newMAP[r][c] = 'X'

for sub in newMAP:
    print(''.join(sub))
    