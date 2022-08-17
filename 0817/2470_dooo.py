n = int(input())
lst = list(map(int, input().split()))

lst.sort()

start = 0
end = n-1
ans = 1e11

while start<end:
    sol = lst[start] + lst[end]
    if abs(sol) < ans:
        ans = abs(sol)
        answer = [lst[start], lst[end]]

    if sol < 0:
        start += 1
    elif sol > 0:
        end -= 1
    else:
        break
print(answer[0], answer[1])