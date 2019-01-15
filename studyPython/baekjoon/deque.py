

import sys

N,M = map(int, input().split())


arr = [ v for v in range(1,N+1)]

pic = list(map(int,sys.stdin.readline().split()))


pos = 0
moveOp = 0 

while len(pic) > 0:
    tmp = pic.pop(0)

    idx = arr.index(tmp)

    if idx > pos:
        distance1 = abs(idx - pos)
        distance2 = abs((len(arr)-idx) + pos)
    else:
        distance1 = abs(pos - idx)
        distance2 = abs((len(arr)-pos) + idx)
        
    
    if distance1 >= distance2:
        moveOp += distance2
    else:
        moveOp += distance1

    arr.pop(idx)
    pos = idx 

print(moveOp)        
        
    



