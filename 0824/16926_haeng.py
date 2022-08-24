def bing(level):
    if level == circle:
        return
    A = bingbing[level][level]
    for i in range(level,M-level-1):
        bingbing[level][i] = bingbing[level][i+1]
    for i in range(level,N-level-1):
        bingbing[i][M-level-1] = bingbing[i+1][M-level-1]
    for i in reversed(range(level+1,M-level)):
        bingbing[N-level-1][i] = bingbing[N-level-1][i-1]
    for i in reversed(range(level+1,N-level)):
        bingbing[i][level] = bingbing[i-1][level]
    bingbing[level+1][level] = A
    bing(level+1)

N,M,R = map(int,input().split())
bingbing = []
for _ in range(N):
    bingbing.append(list(map(int,input().split())))

circle = min(M,N) // 2
while R >0:
    bing(0)
    R -= 1

for i in range(N):
    print(*bingbing[i])


