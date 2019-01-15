import sys


def printDFS(graph,vCnt,sVtx):

    visit = []

    st = []

    st.append(sVtx)
    
    while len(st) > 0:
        pos = st.pop()

        if pos not in visit:
            visit.append(pos)

        edges = graph[pos]

        for e in edges:
            if e not in visit:
                st.append(e)

    print(" ".join(str(v) for v in visit))


def printBFS(graph,vCnt,sVtx):

    visit = []

    que = []

    que.append(sVtx)
    
    while len(que) > 0:
        pos = que.pop(0)

        if pos not in visit:
            visit.append(pos)

        edges = graph[pos]

        for e in edges:
            if e not in visit:
                que.append(e)
    
    print(" ".join(str(v) for v in visit))
                




vCnt,eCnt,stVtx  = list(map(lambda  x: int(x),(input().split())))

graph = dict( zip(range(1,vCnt+1),[[] for _ in range(vCnt)]))


for _ in range(eCnt):
    vtx1,vtx2 = list(map(lambda x: int(x),(sys.stdin.readline().split())))
    (graph[vtx1]).append(vtx2)
    (graph[vtx2]).append(vtx1)

for v in range(1,vCnt+1):
    graph[v].sort(reverse=True)
printDFS(graph,vCnt,stVtx)

for v in range(1,vCnt+1):
    graph[v].sort()
printBFS(graph,vCnt,stVtx)



