import sys
input = sys.stdin.readline

while True:

    R, C = map(int, input().split())
    if R == C == 0: break
    MAP = [[0] * (C + 1)] + [[0] + list(map(int, input().split())) for _ in range(R)]
    memo = [[0] * (C + 1) for _ in range(R + 1)]

    maxV = 0
    for row in range(1, R + 1):
        for col in range(1, C + 1):
            if not MAP[row][col]: continue
            memo[row][col] = min(memo[row][col - 1], memo[row - 1][col], memo[row - 1][col - 1]) + 1
            maxV = max(maxV, memo[row][col])

    print(maxV)
