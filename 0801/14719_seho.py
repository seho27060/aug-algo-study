# 220802 14719 빗물
# 빗물을 세어보자
# h,w <= 500, 250,000
import sys

input= sys.stdin.readline

h,w = map(int,input().split())
heights = list(map(int,input().split()))

limit = [0]*(w)
limit[0] = heights[0]
limit[w-1] = heights[w-1]
for idx in range(1,w-1):
    rSide = max(heights[:idx])
    lSide = max(heights[idx:])
    res = (max(heights[idx],min(rSide,lSide)))
    limit[idx] = res
# print(heights)
# print(limit)
answer = 0
for idx in range(w):
    answer += limit[idx] - heights[idx]
print(answer)