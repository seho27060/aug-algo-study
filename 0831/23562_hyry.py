
# def deegut(sR, sC, K, width):
#
#     cost = 0
#     for row in range(sR, sR + width):
#         for col in range(sC, sC + width):
#             if (0 <= (row - sR) < K) or (K * 2 <= (row - sR)):
#                 if MAP[row][col] == '.':
#                     cost += wb
#             elif K <= (row - sR) < K * 2:
#                 if (col - sC) < K:
#                     if MAP[row][col] == '.':
#                         cost += wb
#                 else:
#                     if MAP[row][col] == '#':
#                         cost += bw
#     # ㄷ의 영역이 아닌 값 계산
#     for row in range(R):
#         for col in range(C):
#             if sR <= row < sR + width and sC <= col < sC + width:
#                 continue
#             if MAP[row][col] == '#':
#                 cost += bw
#     return cost
#
#
# R, C = map(int, input().split())
# wb, bw = map(int, input().split())
#
# MAP = [input() for _ in range(R)]
# maxK = C // 3
#
# minCost = 1e10
# for K in range(1, maxK + 1):
#     width = K * 3
#     # box 시작점
#     for sR in range(R - width + 1):
#         for sC in range(C - width + 1):
#             cost = deegut(sR, sC, K, width)
#             minCost = min(cost, minCost)
#
# print(minCost)

def deegut(sR, sC, K, width):

    cost = 0
    for row in range(R):
        for col in range(C):
            if sR <= row < sR + width and sC <= col < sC + width:
                if (0 <= (row - sR) < K) or (K * 2 <= (row - sR)):
                    if MAP[row][col] == '.':
                        cost += wb
                elif K <= (row - sR) < K * 2:
                    if (col - sC) < K:
                        if MAP[row][col] == '.':
                            cost += wb
                    else:
                        if MAP[row][col] == '#':
                            cost += bw
            elif MAP[row][col] == '#':
                cost += bw
    return cost


R, C = map(int, input().split())
wb, bw = map(int, input().split())

MAP = [input() for _ in range(R)]
maxK = C // 3

minCost = 1e10
for K in range(1, maxK + 1):
    width = K * 3

    for sR in range(R - width + 1):
        for sC in range(C - width + 1):
            cost = deegut(sR, sC, K, width)
            minCost = min(cost, minCost)

print(minCost)