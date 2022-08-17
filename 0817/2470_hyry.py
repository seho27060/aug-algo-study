
import sys

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

i, j = 0, N - 1
ansI = ansJ = minV = sys.maxsize

while i < j:
    sumV = arr[i] + arr[j]
    if sumV == 0:
        print(arr[i], arr[j])
        break
    if sumV > 0:
        if abs(minV) > abs(sumV):
            minV = sumV
            ansI, ansJ = arr[i], arr[j]
        j -= 1
    if sumV < 0:
        if abs(minV) > abs(sumV):
            minV = sumV
            ansI, ansJ = arr[i], arr[j]
        i += 1

else:
    print(ansI, ansJ)
