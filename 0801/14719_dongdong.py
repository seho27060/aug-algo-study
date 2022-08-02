# 백준 14719 빗물

h, w = map(int, input().split())
block = list(map(int, input().split()))
# print(block)

# 특정 위치에서 물이 고이는지 확인하기 위해서는 좌우에 벽이 있는지를 체크해야 함

result = 0
for i in range(1, w-1): # 첫번째와 마지막은 물이 고일 수 없다
    max_left, max_right = -1, -1
    for j in range(i):      # 왼쪽 벽 찾기   i번째 줄 전까지만 검사하면 됨
        if block[j] >= block[i]:    # 새로 탐색하는 j가 크거나 같으면 왼쪽 벽이 될 수 있음
            max_left = max(max_left, block[j])
    for k in range(i+1, w):    # 오른쪽 벽 찾기 i번째 줄 다음 줄부터 검사하면 됨
        if block[k] >= block[i]:    # 새로 탐색하는 K가 크거나 같으면 오른쪽 벽이 될 수 있음
            max_right = max(max_right, block[k])

    if max_left != -1 and max_right != -1:  # 벽이 없는 경우 예외처리
        min_V = min(max_left, max_right)    # 최소 벽의 높이만큼만 물이 찰 수 있음
        result += min_V - block[i]  # 내 위치(i)의 블록 고려, 블록의 높이만큼 빼준다

print(result)
