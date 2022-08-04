# 백준 12852 1로 만들기2

from collections import deque

N = int(input())
Q = deque()
Q.append([N])
ans = []
# print(Q)
while Q:
    # print(Q)
    arr = Q.popleft()
    # print(arr)
    a = arr[0]  # 연산 할 숫자

    if a == 1:
        ans = arr # 계산할 숫자가 1이면 끝
        break

    if a % 3 == 0:
        Q.append([a//3] + arr)  # [a//3]은 다음에 연산할 숫자 3으로 나눠 떨어질 경우
        # print([a//3]+arr)
    if a % 2 == 0:
        Q.append([a//2] + arr)  # [a//2]은 다음에 연산할 숫자 2로 나눠 떨어질 경우

    Q.append([a-1] + arr)   # 1을 뺄 경우

# print(ans)
print(len(ans)-1)   # 배열은 연산의 결과 연산 횟수는 배열길이 -1
for i in range(len(ans)-1, -1, -1): # 큰 수부터 출력해야 됨
    print(ans[i], end = " ")