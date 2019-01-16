

import sys

N = int(input())


triangle = list()

for i in range(N):
    triangle.append(list(map(int,sys.stdin.readline().split())))

    if i == 0 :
        continue

    else:
        for j in range(len(triangle[i])):
            #first index
            if j == 0  :
                triangle[i][j] += triangle[i-1][0]
            #last index
            elif j == len(triangle[i]) -1 :
                triangle[i][j] += triangle[i-1][j-1]

            #mid index
            else:
                triangle[i][j] += max(triangle[i-1][j],triangle[i-1][j-1])


print(max(triangle[-1]))
    
                
