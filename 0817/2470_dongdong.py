# 백준 2470 두 용액 - 투포인터, 이분탐색

'''
투 포인터
- 리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리하는 알고리즘
- 특정한 합을 가지는 부분 연속 수열 문제에 적용 가능
'''

import sys

N = int(input())
arr = sorted(list(map(int, input().split())))  # 정렬 후 양 끝점을 두개의 포인터로 잡아 이동
# print(arr)
minV = sys.maxsize
start = 0  # 시작지점
end = N - 1  # 끝 지점
startV = 0
endV = 0

while start < end:  # 용액의 특성값은 모두 다르기 때문에 start == end는 고려 안해도 됨
    ans = arr[start] + arr[end]  # 두 포인터 더해주기
    if abs(ans) < minV:  # 포인터의 값이 0보다 작으면..
        minV = abs(ans)  # 최솟값 갱신
        startV = arr[start]
        endV = arr[end]

    if ans < 0:  # 계산값이 0보다 작으면 start가 end를 이겨먹고 있는거임
        start += 1  # start 오른쪽 한칸 이동
    elif ans >= 0:  # 반대의 경우 end가 이겨먹고 있음
        end -= 1  # end 왼쪽으로 한칸 이동
    else:  # ans == 0인 경우 찾고 있는 상황
        break

print(startV, endV)
