
basicTriangle = [ "  *  ", " * * ","*****"]
separator = " "
Triangle = list()

def makeTriangle(move,bfTriangle):
    
    # move bfTriangle(root)
    lst = ["   "*move for i in range(len(bfTriangle))]
    rtnLst = list(map(lambda x,y: x+y+x, lst, bfTriangle))
    # add to Child
    rtnLst.extend(list(map(lambda x,y: x+separator+y, bfTriangle, bfTriangle)))
    
    return rtnLst

N = int(input())

if N%3 == 0:
    tmp = int(N/3)

    level = -1
    for i in range(0,11):
        if tmp == pow(2,i):
            level = i
            break

    if level >= 0:
        Triangle2 = basicTriangle.copy()
        for i in range(0,level):
            Triangle2 = makeTriangle(pow(2,i),Triangle2)
            
        for i in Triangle2:
            print(i)

