# 백준 1022 소용돌이 예쁘게 출력하기 - 아 구현인데 이렇게까지 분석이 의미가 있을까 ㅠ 모루겠담....
# 소용돌이 돌리는게 이해 안가는데,,,, 기준점 잡는거까진 ok 그 다음 도는건??

def sol(x, y):
    idx = max(abs(x), abs(y))   # 기준이 되는 인덱스 잡기 한 회전을 하는 배열의 가장 오른쪽 아래 모서리
    before_num = (2 * (idx - 1) + 1) ** 2
    base_num = (2 * idx + 1) ** 2     # 기준점 숫자 구하기, 하나씩 그려보면 규칙이 나온다
    dx, dy = idx - x, idx - y   # 이건 뭘까??

    if x >= y:      # 이 부분을 모르겠다... 손으로 하나씩 써보면 나오는게 확인이 되는데 원리는??
        return base_num - dx - dy   # 왜 이때는 현재 기준점에서 빼주고    x >= y이면 현재 base에서 계산
    else:
        return before_num + dx + dy     # 왜 이때는 이전 기준점에서 더할까??  # 오른쪽으로 이동이라 시계방향 -> 하나씩 작아져야 한다...
        # 아니면 이전 기준점에서 계산이 들어가야 한다...

r1, c1, r2, c2 = map(int, input().split())
arr = []    # 숫자 저장 배열
for i in range(r1, r2 +1):
    tmp = []
    for j in range(c1, c2+1):
        tmp.append(sol(i, j))   # 범위 안에서만 소용돌이 돌리기
    # print(tmp)
    arr.append(tmp)
# print(arr)

max_v = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        max_v = max(max_v, arr[i][j])

for i in range(len(arr)):
    for j in range(len(arr[i])):
        sub = len(str(max_v)) - len(str(arr[i][j]))
        if sub > 0:
            print(' ' * sub, end='')    # 수의 길이가 가장 길이가 긴 수보다 작다면 공백을 삽입해 길이를 맞추자.. 출력의 문제!!
        print(arr[i][j], end=' ')
    print('')
