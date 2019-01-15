
def procErasto(maxVal):
    rfTable = [ 1 for i in range(0,maxVal+1)]
    rfTable[0]= 0 
    rfTable[1]= 0
    
    for n in range(2,int(maxVal**0.5)+1):
        for r in range(2,maxVal//n+1):
            rfTable[n*r] = 0
    
    return rfTable



rfTable = procErasto(123456*2)
n = int(input())
while n != 0:
   
    print (sum(rfTable[n+1:n*2+1]))
    n = int(input())
