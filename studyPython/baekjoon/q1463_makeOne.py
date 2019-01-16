
memo = [0] *1000001

def MakeOneCntMemo(N):

    check = list()
    if N % 3 == 0 :
        check.append(memo[N//3]+1)
    
    if N % 2 == 0:
        check.append(memo[N//2]+1)

    check.append(memo[N-1]+1)

    memo[N] = min(check)


N = int(input())

memo[2] = 1
memo[3] = 1

if N > 3:
    for i in range(4,N+1):
        MakeOneCntMemo(i)


print(memo[N])




