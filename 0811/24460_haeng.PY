import sys
sys.setrecursionlimit(10**6)

N=int(input())

A = []
for _ in range(N):
    A.append(list(map(int,input().split())))
def NNN(x,y,long):
    if long == 1:
        return A[y][x]
    B = []
    long = long//2
    B.append(NNN(x, y, long))
    B.append(NNN(x+long, y, long))
    B.append(NNN(x, y+long, long))
    B.append(NNN(x+long, y+long, long))
    B.sort()
    return B[1]
print(NNN(0,0,N))