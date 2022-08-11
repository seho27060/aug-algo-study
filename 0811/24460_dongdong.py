# 백준 24460 특별상이라도 받고 싶어 - 분할정복 왜?

'''
분할 정복 - 문제를 여러개로 분할하여 정복하기
1. 분할 : 문제를 작은 문제로 분할하는 과정
2. 정복 : 분할한 작은 문제들을 해결
3. 조합 : 작은 문제에 대한 결과를 원본 문제에 대한 결과로 조립
'''

def sol(size, x, y):
    if size == 1:   # 탐색 사이즈가 1이면 볼거도 없음
        return arr[x][y]
    else:
        # 각 사분면을 기준으로 분할한다
        nbs = size // 2
        lst = []    # 결과를 받아 줄 리스트
        # 1
        lst.append(sol(nbs, x, y))
        # 2
        lst.append(sol(nbs, x, y+nbs))
        # 3
        lst.append(sol(nbs, x+nbs, y))
        # 4
        lst.append(sol(nbs, x+nbs, y+nbs))
        lst.sort()
        # print(lst)
        return lst[1]   # 두번째 값 꺼내기


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)

print(sol(N, 0, 0)) # N = 탐색 범위  , x, y = 각 탐색의 좌표를 가지는 변수
