dx=[1,-1,0,0]
dy=[0,0,1,-1]
def apple(level,nowJx,nowJy,nowHx,nowHy):
    global J,H,result
    if level == (24-K)//2:
        result += 1
        return


    for i in range(4):
        Jx = nowJx + dx[i]
        Jy = nowJy + dy[i]
        if 0<=Jx< 5 and 0<=Jy< 5 and tree[Jy][Jx] ==0:
            for i in range(4):
                Hx = nowHx + dx[i]
                Hy = nowHy + dy[i]
                if 0 <= Hx < 5 and 0 <= Hy < 5 and tree[Hy][Hx] == 0:
                    if level < (24-K)//2-1 and (Jx,Jy)==(Hx,Hy): continue
                    tree[Hy][Hx] = 1
                    tree[Jy][Jx] = 1
                    apple(level+1,Jx,Jy,Hx,Hy)
                    tree[Hy][Hx] = 0
                    tree[Jy][Jx] = 0


tree = [[0]*5 for _ in range(5)]
K = int(input())
for _ in range(K):
    y,x = map(int,input().split())
    tree[y-1][x-1] = 1

result = 0
tree[0][0] = 1
tree[4][4] = 1
apple(0,0,0,4,4)

print(result)