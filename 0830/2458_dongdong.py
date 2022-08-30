# 백준 2458 키순서  - 플로이드 와샬
# 플로이드 와샬 - 모든 정점에서 모든 정점으로의 최단경로를 구할 때 사용
# 플로이드 와샬을 각 노드에서 다른 모든 노드로 연결이 되어 있는지 체크하는 용도로 사용

N, M = map(int, input().split())
arr = [[0]*N for _ in range(N)] # 연결 여부를 저장하기 위한 배열, 노드의 갯수만큼 만들어주기

for _ in range(M):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1   # 연결이 되어 있음을 표시
# print(arr)

# 플로이드와샬 점화식 가운데 노드가 반목문의 최상단에 위치!!!
for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][k] == 1 and arr[k][j] == 1:   # 1 -> 2 노드와 2 -> 3 노드가 연결되어 있으면
                arr[i][j] = 1   # 1 -> 3도 연결되어 있음 플로이드와샬 점화식 이용


# print(arr)
result = 0
# 한 노드와 연결된 노드의 갯수가 N-1개라면 그 노드는 모든 노드를 방문하기 때문에 키 비교가 가능하다
for i in range(N):  # 한 노드씩 체크
    cnt = 0
    for j in range(N):
        cnt = cnt + arr[i][j] + arr[j][i]   # 한 노드가 다른 노드를 방문하는지 모조리 체크
    if cnt == N-1:  # 모든노드를 방문하면
        result += 1 # 결과값 +1
print(result)
