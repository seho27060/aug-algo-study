# 백준 9465 스티커 - dp
# 스티커 하나 떼면 스티커와 변을 공유하는 스티커 모두 뜯어짐,, 어느 스티커로 이동할 수 있느냐를 체크

T = int(input())    # 테스트케이스 갯수,, 백준에서 스웨아 스타일 문제라니...

for _ in range(T):
    n = int(input())    # 한 줄에 몇개의 스티커가 있을까??
    arr = [] # 점수 저장 배열
    for _ in range(2):  # 두 줄에 걸쳐서 스티커 점수 input
        arr.append(list(map(int, input().split())))
    # print(arr)

    if n == 1:
        print(max(arr[0][0], arr[1][0]))    # 한 줄에 하나씩이면 그냥 두개 값 중 큰게 답
        continue

    # 스티커 떼는건 대각선으로밖에 이동이 안된다. 시작할 수 있는 경우 두가지임
    arr[0][1] += arr[1][0]
    arr[1][1] += arr[0][0]

    for i in range(2, n):
        # 이차원 배열을 그려서 생각해보자,, 바로 옆에 있는건 못떼니까 한 줄 밑에 있는 대각선 방향 두개 중 큰 값을 더해준다..
        arr[0][i] += max(arr[1][i-1], arr[1][i-2])
        # 바로 옆에 있는건 못떼니까 대각선 방향 한줄 위에 것들을 선택
        arr[1][i] += max(arr[0][i-1], arr[0][i-2])

    # print(arr)
    # 맨 마지막 값 중 큰 것 출력
    print(max(arr[0][n-1], arr[1][n-1]))

