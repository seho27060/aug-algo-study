N = int(input())
chair = [list(map(int, input().split())) for _ in range(N)]

def solve(x, y, n):
    if n == 1:
        return chair[x][y]
    else:
        n //= 2
        lst = []
        lst.append(solve(x, y, n))
        lst.append(solve(x, y+n, n))
        lst.append(solve(x+n, y, n))
        lst.append(solve(x+n, y+n, n))
        lst.sort()
        return lst[1]

print(solve(0, 0, N))