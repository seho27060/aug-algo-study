import sys
input = sys.stdin.readline

def solve(node, tmp, time):
    global ans
    if tmp == n:
        ans = min(ans, time)
        return
    for next_node in range(n):
        if not visit[next_node]:
            visit[next_node] = 1
            solve(next_node, tmp + 1, time + graph[node][next_node])
            visit[next_node] = 0

n, k = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))

visit = [0]* n
ans = sys.maxsize
visit[k] = 1

for p in range(n):
    for q in range(n):
        for r in range(n):
            graph[q][r] = min(graph[q][r], graph[q][p] + graph[p][r])

solve(k, 1, 0)
print(ans)