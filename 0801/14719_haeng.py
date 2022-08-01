H,W = map(int,input().split())
tower = list(map(int,input().split()))

result = 0
for y in range(1,H+1):
    s=0
    cnt = 0
    for x in range(W):
        if tower[x] >= y and s ==0:
            s=1
        elif tower[x] >= y and s == 1:
            result += cnt
            cnt = 0
        elif tower[x] < y and s:
            cnt += 1
print(result)
