# 220817 2470 두 용액
# n <= 100,000/ 이진탐색?

import sys

input = sys.stdin.readline

n = int(input())

lst = list(map(int,input().split()))
lst.sort()
start = 0
end = n-1
answer = [float("inf"),-1,-1]
while start < end:
    result = lst[start] + lst[end]
    # print(result,lst[start],lst[end])
    if answer[0] > abs(result):
        answer = [abs(result),lst[start],lst[end]]
    if result < 0:
        start += 1
    if result >= 0:
        end -= 1
print(*answer[1:])
