import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(x, y, n):
    if n == 1:
        return arr[x][y]
    if n == 2:
        ans = []
        ans.append(arr[x][y])
        ans.append(arr[x][y+1])
        ans.append(arr[x+1][y])
        ans.append(arr[x+1][y+1])

        ans.sort()
        return ans[1]


    lst = []
    lst.append(dfs(x,y,n//2))
    lst.append(dfs(x,y+n//2,n//2))
    lst.append(dfs(x+n//2,y,n//2))
    lst.append(dfs(x+n//2,y+n//2,n//2))

    lst.sort()

    return lst[1]

print(dfs(0,0,n))


