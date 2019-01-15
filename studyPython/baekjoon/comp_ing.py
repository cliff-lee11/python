
import sys

def comp(N,K):
    # nCr = (n-r+1)/r * nCr-1
    # nC0 = 1 ( r ==0)

    if K == 0 :
        return 1

    rtnVal = 1

    
    if K > N//2:
        K = N-K
        
    for r in range(1,K+1):
        rtnVal = rtnVal * (N-r +1)//r

    return rtnVal
        
    

while True:
    
    N,K = list(map(int,sys.stdin.readline().split()))

    if N == 0 and K == 0 :
        break

    print(comp(N,K))
