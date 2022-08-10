#좌상4, 좌하6 우하8 우상2
#대각선으로 접근해서 해당 자리값 구하기
def DDDD(x,CCCCC):
    A = 1
    c = 0
    for i in range(x):
        if i == 0:
            A += CCCCC
            c = CCCCC
        else:
            c += 8
            A += c
    return A

def NNNNNN(x,NN):
    c = 0
    for i in range(x):
        if i == 0:
            c = NN
        else:
            c += 8
    return c


def find(y,x):
    if abs(y) > abs(x):
        D = abs(y)
        M = x
    else:
        D = abs(x)
        M = y


    if y>=0 and x>=0:    #4사분면
        E = DDDD(D,8)
        if M == x:
            return E-(y-x)
        else:
            F = E-NNNNNN(D,7)
            return F+x-(y+1)

    elif y>=0 and x<=0:  #3사분면
        E = DDDD(D,6)
        if M == y:
            return E+(x+y)
        else:
            F = E + (y-abs(x))
            return F

    elif y<=0 and x<=0:  #2사분면
        E = DDDD(D,4)
        if M == x:
            return E - (abs(x-y))
        else:
            return E + (abs(x-y))

    elif y<=0 and x>=0:  #1사분면
        E = DDDD(D,2)
        if M == x:
            return E + (abs(x + y))
        else:
            return E - (abs(x + y))




r1,c1,r2,c2 = map(int,input().split())


result = []
long = 0
for y in range(r1,r2+1):
    H = []
    for x in range(c1,c2+1):
        RRR = str(find(y,x))
        if len(RRR) > long:
            long = len(RRR)
        H.append(RRR)
    result.append(H)



for y in range(r2+1-r1):
    for x in range(c2+1-c1):
        if len(result[y][x]) < long:
            if x == c2-c1:
                print(' ' * (long - len(result[y][x])) + result[y][x])
            else:
                print(' '*(long-len(result[y][x]))+result[y][x], end=" ")
        else:
            if x == c2-c1:
                print(result[y][x])
            else:
                print(result[y][x], end=" ")