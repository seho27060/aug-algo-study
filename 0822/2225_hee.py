import math

N, M = map(int, input().split())
print(math.factorial(N+M-1)//(math.factorial(M-1) * math.factorial(N)) % 10**9)