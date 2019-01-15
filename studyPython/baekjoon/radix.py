import sys

def radixSort(lst,maxRadix):

    for rIndex  in range(maxRadix+1):

        intTable = [ list() for i in range(10)]
        
    
        for v in lst:
            tmp = str(v)
            if len(tmp) >= rIndex:         
                intTable[int(tmp[rIndex*-1])].append(v)
            else:
                intTable[0].append(v)
        
        
        index = 0
        for i in intTable:
            for j in i:
                lst[index] = j
                index = index+1

      #  print(intTable)

    for e in lst:
        print(e)
        

NC = int(input())

lst  = list()
maxVal  = -1
for i in range(0,NC):
    nVal = sys.stdin.readline().rstrip()
    lst.append(nVal)
    if(maxVal < int(nVal)):
        maxVal = int(nVal)


radixSort(lst,len(str(maxVal)))
         
    
    
