# DP문제
# 양 옆의 숫자는 선택할 수 없으므로 대각선을 고려하며 DP를 설계

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    s = [list(map(int,input().split())) for _ in range(2)]
    for i in range(1, n):
        if i == 1:
            s[0][i] += s[1][i-1]
            s[1][i] += s[0][i-1]
        else:
            s[0][i] += max(s[1][i-1], s[1][i-1])
            s[1][i] += max(s[0][i-1], s[0][i-2])
        print(max(s[0][n-1], s[1][n-1]))