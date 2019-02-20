'''
Created on 2019. 2. 20.

@author: jhlee
 소수 판별 
 
'''


import sys

T = int(input())

Tlst = list()

for i in range(T):
    Tlst.append(int(sys.stdin.readline().rstrip()))


for v in Tlst:

    isPrime = True

    if v == 1:
        isPrime = False

    for i in range(2,int(v**0.5)+1):
        if v%i == 0 :
            isPrime = False
            break
      

    if isPrime== True:
        print("Prime")
    else:
        print("Not prime")
        