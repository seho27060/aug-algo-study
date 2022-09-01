n, m = map(int, input().split())
a, b = map(int, input().split())
arr = [list(input()) for _ in range(n)]
k = min(n, m)//3

ans = 1e10
for c in range(1, k+1):
    for x in range(n-(c*3)+1):
        for y in range(m-(c*3)+1):
            res = 0
            for i in range(n):
                for j in range(m):
                    if x<=i<x+c and y<=j<y+c*3:
                        if arr[i][j] == '.':
                            res += a
                    elif x+c*2<=i<x+c*3 and y<=j<y+c*3:
                        if arr[i][j] == '.':
                            res += a
                    else:
                        if x+c<=i<x+c*2 and y<=j<y+c:
                            if arr[i][j] == '.':
                                res += a
                        else:
                            if arr[i][j] == '#':
                                res += b
            ans = min(ans, res)
print(ans)