import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

for i in range(n):
    arr[i].insert(0, '.')
    arr[i].append('.')

arr.insert(0, ['.'] * (m+2))
arr.append(['.'] * (m+2))
n += 2
m +=2

ans = copy.deepcopy(arr)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'X':
            cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] == '.':
                        cnt +=1

            if cnt >= 3:
                ans[i][j] = '.'


start= 0
end = 0
rs = 0
re = 0
def fs():
    global start
    for j in range(m):
        for i in range(len(ans)):
            if ans[i][j] == 'X':
                start = j
                return
def fe():
    global end
    for j in range(m-1, -1, -1):
        for i in range(len(ans)):
            if ans[i][j] == 'X':
                end = j
                return
def sr():
    global rs
    for i in range(n):
        if 'X' in ans[i]:
            rs = i
            return
def er():
    global re
    for i in range(n-1,-1,-1):
        if 'X' in ans[i]:
            re = i
            return


fs()
fe()
sr()
er()
for i in range(rs, re+1):
    for j in range(start, end + 1):
        print(ans[i][j], end = '')
    print()
