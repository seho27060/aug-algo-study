# 220831 23562 ㄷ만들기
import sys

input = sys.stdin.readline

# 검은칠 a
def makediguet1(sr,sc,k):
    global n,m,a,b,board,visited,result

    for row in range(sr, sr+k):
        for col in range(sc,sc+3*k):
            if board[row][col] == ".":
                visited[row][col] = a
                result += a
            else:
                visited[row][col] = 0

    # for kk in visited:
    #     print(kk)
    # print("__________________________")

# 3분의1은검은칠 a/나머지흰칠 b
def makediguet2(sr, sc, k):
    global n, m, a, b, board, visited, result

    for row in range(sr,sr+k):
        for col in range(sc,sc+k):
            if board[row][col] == ".":
                visited[row][col] = a
                result += a
            else:
                visited[row][col] = 0
        for col in range(sc+k+1,sc+3*k):
            if board[row][col] == "#":
                visited[row][col] = b
                result += b
            else:
                visited[row][col] = 0
    # for kk in visited:
    #     print(kk)
    # print("__________________________")
# 칠한 나머지 흰칠 b
def clearOthers(sr,sc):
    global n, m, a, b, board, visited, result

    for row in range(n):
        for col in range(m):
            if visited[row][col] == -1:
                if board[row][col] == "#":
                    visited[row][col] = b
                    result += b
                else:
                    visited[row][col] = 0
    # for kk in visited:
    #     print(kk)
    # print("__________________________")


n, m = map(int,input().split())
a, b = map(int,input().split())
board = [list(input()) for _ in range(n)]
#  넓이가 어떻든 ㄷ하나만 만들면 됨.
# k = min(n,m)//3+1
answer = float("inf")
for K in range(1,min(n,m)//3+1):
    for row in range(n-3*K+1):
        for col in range(m-3*K+1):
            visited = [[-1] * (m) for _ in range(n)]
            result = 0
            makediguet1(row,col,K)
            makediguet2(row+K,col,K)
            makediguet1(row+2*K,col,K)
            clearOthers(row,col)
            # print("************************", row,col,K)
            # print("***********************", answer,result)
            answer = min(answer,result)

print(answer)