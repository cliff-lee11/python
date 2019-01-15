'''
fib(5) = fib(4) + fib(3)

fib(4) = fib(3) + fib(2)
fib(3) = fib(2) + fib1(1)
fib(2) = fib(1) + fib(0)
fib(1) = 1
fib(0) = 1
'''

import sys

def prnFibInfo(v):

    fibinfo = []
    fibinfo.append((1,0))
    fibinfo.append((0,1))

    if v >= 2:
        for f in range(2,v+1):
            tmp1 = fibinfo[f-1][0] + fibinfo[f-2][0]
            tmp2 = fibinfo[f-1][1] + fibinfo[f-2][1]
            fibinfo.append((tmp1,tmp2))


    print(fibinfo[v][0],fibinfo[v][1])
    
    

T = int(input())

for _ in range(T):
    prnFibInfo(int(sys.stdin.readline()))




