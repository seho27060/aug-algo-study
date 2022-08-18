while 1:
    N,M = map(int,input().split())
    if N==0 and M ==0:
        break

    A = []
    for _ in range(N):
        A.append(list(map(int,input().split())))


    result = 0
    for i in range(N):
        if A[i][0]:
            result = 1
    for j in range(M):
        if A[0][j]:
            result = 1

    for y in range(1,N):
        for x in range(1,M):
            if A[y][x]:
                b = min(A[y-1][x-1],A[y-1][x],A[y][x-1])
                A[y][x] = b+1
                if result < b+1:
                    result = b+1

    print(result)