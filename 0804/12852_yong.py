# DP를 활용한 문제
# 1부터 N까지 DP를 활용하여 최단 횟수를 구한다
# N부터 1까지 내려가며 1 작거나 2, 3으로 나눠지는 수와 DP차이가1인경우 리스트에 저장하고 탐색 위치를 옮긴다.

N = int(input())
DP = [-1] * (N+1)
DP[1] = 1 
for i in range(1, N):
    if i * 3 <= N:
        if DP[i*3] == -1 or DP[i*3] > DP[i] + 1:
            DP[i*3] = DP[i] + 1
    if i * 2 <= N:
        if DP[i*2] == -1 or DP[i*2] > DP[i] + 1:
            DP[i*2] = DP[i] + 1
    if DP[i+1] == -1 or DP[i+1] > DP[i] + 1:
        DP[i+1] = DP[i] + 1
cnt = 0
ans = [N]
val = N
while True:
    if val == 1:
        print(cnt)
        print(*ans)
        break
    if val % 3 == 0:
        if DP[val] - DP[val//3] == 1:
            val = val//3
            ans.append(val)
            cnt += 1
            continue
    if val % 2 == 0:
        if DP[val] - DP[val//2] == 1:
            val = val//2
            ans.append(val)
            cnt += 1
            continue
    if DP[val] - DP[val-1] == 1:
        val -= 1
        ans.append(val)
        cnt += 1
        continue