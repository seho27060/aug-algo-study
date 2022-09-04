# 백준 23562 ㄷ만들기
import sys
INF = sys.maxsize
# .은 흰 , # 은 검

def f(x, y, k):
    cnt = 0
    # 디귿이 될 수 없는 범위를 뽑아야 된다.... 이게 너무 어려운데 하나씩 그려보면 나오는데 어떻게 도출이 되는지 정확히 모르겠는뎁....
    # 일단 (x, y) ~ (x+3k-1, y+3k-1)의 영역은 전부 검은색이어야 됨
    # 내부 공백 처리 =>
    for i in range(n):
        for j in range(m):
            if x <= i < x + k and y <= j < y + k * 3:
                if arr[i][j] == ".":
                    cnt += a
            elif x + k * 2 <= i < x + k * 3 and y <= j < y + k * 3:
                if arr[i][j] == ".":
                    cnt += a
            else:
                if x + k <= i < x + k * 2 and y <= j < y + k:   #
                    if arr[i][j] == ".":
                        cnt += a
                else:
                    if arr[i][j] == "#":    # 범위 밖 검은 색은 전부 흰색으로 만들어주기
                        cnt += b
    return cnt

n, m = map(int, input().split())
a, b = map(int, input().split())    # a = 흰 -> 검 b = 검 -> 흰
arr = []
for _ in range(n):
    arr.append(list(input()))
# print(arr)
# ㄷ은 3k * 3k 안에서 만들어진다
K = min(n, m) // 3
cost = INF
for k in range(1, K+1):
    for x in range(n-k*3+1):
        for y in range(m-k*3+1):
            result = f(x, y, k)
            if result <= cost:
                cost = result

print(cost)
