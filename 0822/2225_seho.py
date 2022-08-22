# 220822 2225 합분해
# 0 ~ n 의 정수 k개를 더해 그 합이 n이 되는 경우의 수 구하기
# 덧셈 순서 바뀌면 다른 경우, 한개의 수 여러번 사용 가능
# n < 200, k < 200

import sys

input = sys.stdin.readline

n, k = map(int,input().split())
t = 1
d= 1
answer = 1

for nxt in range(1,k):
    t *= n+k-nxt
    d *= nxt
answer = (t//d)%1000000000
print(answer)