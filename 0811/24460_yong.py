# 재귀를 활용하여 답을 구하는 문제
# 각 사분면을 계속 탐색해 값을 가져온 뒤 2번째 높은 값을 찾는다.

def find(x, y, l):
    if l == 1:
        return arr[y][x]
    lst = []
    l = l//2
    lst.append(find(x, y, l))
    lst.append(find(x+l, y, l))
    lst.append(find(x, y+l, l))
    lst.append(find(x+l, y+l, l)) 
    lst.sort()
    return lst[1]   
    
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

print(find(0, 0, N))