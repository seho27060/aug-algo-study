H, W = map(int, input().split())
A = list(map(int, input().split()))

G = [[0] * W for _ in range(H)]
for i in range(W):
    for j in range(A[i]):
        G[j][i] = 1
cnt = 0
for i in range(H):
    for j in range(1, W):
        if not G[i][j] and G[i][j-1]:
            temp = 0
            while True:
                if W <= j:
                    temp = 0
                    break

                if G[i][j]:
                    break

                temp += 1
                j += 1
            cnt += temp
print(cnt)