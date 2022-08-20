######################
import sys
sys.setrecursionlimit(10**5)

def findSum(key, sumV):
    if sumV >= N or key == K: return sumV == N
    if (key, sumV) in memo: return memo[(key, sumV)]

    for num in range(N + 1):
        memo[(key, sumV)] = (
            memo.get((key, sumV), 0) + findSum(key + 1, sumV + num)
        ) % 1_000_000_000

    return memo[(key, sumV)]

memo = dict()

ans = findSum(0, 0)
print(ans)

#######################
N, K = map(int, input().split())
memo = [[0] * (N + 1) for _ in range(K + 1)]

for num in range(N + 1):
    memo[1][num] = 1

for k in range(2, K + 1):
    for num in range(N + 1):
        for subNum in range(num + 1):
            memo[k][num] += memo[k - 1][subNum]
        memo[k][num] %= 1_000_000_000

print(memo[K][N])