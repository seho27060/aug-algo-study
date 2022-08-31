def check(x,y,k):
    cnt = 0
    for y2 in range(N):
        for x2 in range(M):
            if (y<= y2 < y+k or y+k*2 <= y2< y+k*3) and x<=x2<x+k*3:
                if PAPER[y2][x2] == '.':
                    cnt += B
            elif x<= x2 < x+k and y<=y2<y+k*3:
                if PAPER[y2][x2] == '.':
                    cnt += B
            else:
                if PAPER[y2][x2] == '#':
                    cnt += W
    return cnt


N,M = map(int,input().split())
B,W = map(int,input().split())

PAPER = []
for _ in range(N):
    PAPER.append(list(input()))

# k의 최댓값 = min(N,M) / 3
K = min(N,M) // 3

# 0부터 N - K*3

result = 99999999999999
for k in range(1,K+1):
    for y in range(N-k*3+1):
        for x in range(M-k*3+1):
            #해당 좌표에서 k 크기의 사각형을 만드는 비용 체크
            if check(x,y,k) < result:
                result = check(x,y,k)
print(result)