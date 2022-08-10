r1, c1, r2, c2 = map(int, input().split())
arr = [[0]*(c2-c1+1) for _ in range(r2-r1+1)]
k = (r2-r1+1)*(c2-c1+1)

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dd = 0
dcnt = 1
tmp = 1
x, y = 0, 0
maxlV = 0
cnt = 0
while k>0:
    if r1<=x<=r2 and c1<=y<=c2:
        arr[x-r1][y-c1] = tmp
        k -= 1
        if maxlV < len(str(tmp)):
            maxlV = len(str(tmp))

    tmp += 1
    dx, dy = d[dd]
    x += dx
    y += dy
    cnt += 1

    if cnt == dcnt:
        cnt = 0
        dd = (dd+3)%4
        if dd == 0 or dd == 2:
            dcnt += 1

for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        p = str(arr[i][j])
        if len(p) == maxlV:
            print(arr[i][j], end=' ')
        else:
            lV = maxlV-len(p)
            space = ' '*(lV)
            print(f'{space}{p}', end=' ')
    print()