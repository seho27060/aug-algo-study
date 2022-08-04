# 220804 12852 1로 만들기 2
# 3으로 나누어떨어져/ 2로 나누어쪌어져/1 빼기
# 3개 연산으로 1을 만들려고할때 가장 빠르게만드는 연산 순서 출력
# 백트래킹?bfs?
# n <= 1,000,000

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
answer = 0
visited = [0 for _ in range(n+1)]
queue = deque([1])
while queue:
    now = queue.popleft()
    if now*3 <= n and not visited[now*3]:
        visited[now*3] = now
        queue.append(now*3)
    if now * 2 <= n and not visited[now * 2]:
        visited[now * 2] = now
        queue.append(now * 2)
    if now +1 <= n and not visited[now + 1]:
        visited[now + 1] = now
        queue.append(now + 1)
answer = [n]
# print(visited)
# print(answer)
while answer[-1] != 0:
    answer.append(visited[answer[-1]])
print(len(answer)-2)
print(*sorted(answer[:-1],reverse=True))