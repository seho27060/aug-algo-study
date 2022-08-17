N = int(input())
A = list(map(int,input().split()))

A.sort()

L = 0
R = N-1

result = [2000000001,0,N-1]
while L<R:
    P = A[L]+A[R]
    if abs(P) < result[0]:
        result = [abs(P),L,R]

    if P == 0:
        break
    elif P > 0:
        R -= 1
    else:
        L += 1

print(A[result[1]],A[result[2]])