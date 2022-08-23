
import sys
input = sys.stdin.readline

R, C, cnt = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
ans = [[0] * C for _ in range(R)]

for start in range(min(R, C) // 2):
    lineCnt = ((R - start * 2) - 1 + (C - start * 2) - 1) * 2
    arr = [0] * lineCnt
    rest = cnt % lineCnt

    # arr 기본으로 채워 넣기
    r = c = start
    idx = 0
    arr[idx] = MAP[start][start]

    for i in range(1, R - start * 2):
        idx += 1
        r += 1
        arr[idx] = MAP[r][c]

    for i in range(1, C - start * 2):
        idx += 1
        c += 1
        arr[idx] = MAP[r][c]

    for i in range(1, R - start * 2):
        idx += 1
        r -= 1
        arr[idx] = MAP[r][c]

    for i in range(1, C - start * 2 - 1):
        idx += 1
        c -= 1
        arr[idx] = MAP[r][c]

    # 회전
    newArr = [0] * lineCnt
    for idx in range(lineCnt):
        newArr[(idx + rest) % lineCnt] = arr[idx]

    # 답 생성하기
    ansR = ansC = start
    ansIdx = 0
    ans[start][start] = newArr[0]

    for i in range(1, R - start * 2):
        ansIdx += 1
        ansR += 1
        ans[ansR][ansC] = newArr[ansIdx]

    for i in range(1, C - start * 2):
        ansIdx += 1
        ansC += 1
        ans[ansR][ansC] = newArr[ansIdx]

    for i in range(1, R - start * 2):
        ansIdx += 1
        ansR -= 1
        ans[ansR][ansC] = newArr[ansIdx]

    for i in range(1, C - start * 2 - 1):
        ansIdx += 1
        ansC -= 1
        ans[ansR][ansC] = newArr[ansIdx]


for row in range(R):
    print(*ans[row])
