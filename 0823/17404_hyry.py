import sys
input = sys.stdin.readline

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

red = [[1e10] * 3 for _ in range(N)]
blue = [[1e10] * 3 for _ in range(N)]
green = [[1e10] * 3 for _ in range(N)]

red[0] = [*MAP[0]]
green[0] = [*MAP[0]]
blue[0] = [*MAP[0]]
red[0][0] = green[0][1] = blue[0][2] = 1e10

for idx in range(1, N):
    for color in range(3):
        red[idx][color] = MAP[idx][color] + min(
            red[idx - 1][0] if color != 0 else 1e10,
            red[idx - 1][1] if color != 1 else 1e10,
            red[idx - 1][2] if color != 2 else 1e10
        )
        green[idx][color] = MAP[idx][color] + min(
            green[idx - 1][0] if color != 0 else 1e10,
            green[idx - 1][1] if color != 1 else 1e10,
            green[idx - 1][2] if color != 2 else 1e10
        )
        blue[idx][color] = MAP[idx][color] + min(
            blue[idx - 1][0] if color != 0 else 1e10,
            blue[idx - 1][1] if color != 1 else 1e10,
            blue[idx - 1][2] if color != 2 else 1e10
        )

print(min(red[N - 1][0], green[N - 1][1], blue[N - 1][2]))