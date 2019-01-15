
import sys
from operator import itemgetter


def prnInfo(N,M,prLst):

    prnSeq = 0

    if M > len(prLst):
        return None

    check = prLst[M]
    
    while len(prLst) > 0:
        p = prLst[0]
        if p[1] == max(prLst,key=itemgetter(1))[1]:
            if p[0] == check[0]:
                return prnSeq+1
            else:
                prLst.pop(0)
                prnSeq+=1
                
        else:
            tmp = prLst.pop(0)
            prLst.append(tmp)
            
            
            


TC = int(input())


for _ in range(TC):
    N,M = map(int,sys.stdin.readline().split())
    prLst = list(zip([seq for seq in range(1,N+1)],list(map(int,sys.stdin.readline().split()))))
    print(prnInfo(N,M,prLst))
