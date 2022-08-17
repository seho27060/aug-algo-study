import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

S, E = 0, N-1

min_val, max_val, diff = 0, 0, sys.maxsize

while S < E:
  if abs(A[S] + A[E]) < diff:
    min_val, max_val, diff = A[S], A[E], abs(A[S] + A[E])
  if A[S] + A[E] == 0:
    break
    
  elif A[S] + A[E] < 0:
    S += 1

  else:
    E -= 1

print(min_val, max_val)