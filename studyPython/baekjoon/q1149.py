

N = int(input())

cinfo = []
for _ in range(N):
    cinfo.append(list( map(int,input().split())))


for i in range(1, N):
    #min Red
    cinfo[i][0] = cinfo[i][0] + min(cinfo[i-1][1], cinfo[i-1][2])
    #min Green
    cinfo[i][1] = cinfo[i][1] + min(cinfo[i-1][0], cinfo[i-1][2])
    #min Blue
    cinfo[i][2] = cinfo[i][2] + min(cinfo[i-1][0], cinfo[i-1][1])


print(min(cinfo[-1]))
