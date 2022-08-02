n, m = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
for i in range(1,m-1):
    left = max(lst[:i])
    right = max(lst[i+1:])
    stdd = min(left, right)
    if stdd > lst[i]:
        ans += stdd - lst[i]
print(ans)