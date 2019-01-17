'''
계단 오르는 데는 다음과 같은 규칙이 있다.

계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
마지막 도착 계단은 반드시 밟아야 한다.
따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 
하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 
첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.

각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.

입력
입력의 첫째 줄에 계단의 개수가 주어진다.

둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다. 
계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.

출력
첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 출력한다.

예제 입력 1 
6
10
20
15
25
10
20

출력 
75 
'''
import sys 

def calMaxScore(stairs):
    '''  마지막 계단은 밟아야 함 
    stair[N] 에 도착 하려면, 
        1. stair[N-1] -> stair[N]
                  =>  여기서  stair[N-2]는 밟으면 안된다. 즉 Stair[N-1]을 밟았다면, Stair[N-3]을 밟아야 한다. 
        2. stair[N-2] -> stair[N]
               
               즉  어떤 계단 N까지 가려면,  stair[N-3] + stair[N-1] + Stair[N]
                             stair[N-2] + Stair[N]
    
    '''
    step = []
    step.append(stairs[-1])
    
    pos = len(stairs)-1
    while pos >= 3:
        tmp1 = stairs[pos-3] + stairs[pos-1]
        tmp2 = stairs[pos-2]
        
        if tmp1 > tmp2:
            step.append(stairs[pos-1])
            step.append(stairs[pos-3])
            pos = pos -3
            
        else:
            step.append(stairs[pos-2])
            pos = pos -2
        
        
    print(step)
    return sum(step) 
     
    
N = int(input())

stairs = [0]

for _ in range(N):
    stairs.append(int(sys.stdin.readline()))

print(calMaxScore(stairs))




