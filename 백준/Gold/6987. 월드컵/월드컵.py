from itertools import combinations
import sys

def dfs(x,y):
    global L, tmp
    
    if y==6:
        x+=1
        y=x+1
    
    if x==5:
        if L==[[0,0,0] for _ in range(6)]:
            tmp=1
        return

    #x가 이긴경우
    if L[x][0]>0 and L[y][2]>0:
        L[x][0], L[y][2] = L[x][0]-1, L[y][2]-1
        dfs(x,y+1)
        L[x][0], L[y][2] = L[x][0]+1, L[y][2]+1
    
    #x가 지는경우
    if L[x][2]>0 and L[y][0]>0:
        L[x][2], L[y][0] = L[x][2]-1, L[y][0]-1
        dfs(x,y+1)
        L[x][2], L[y][0] = L[x][2]+1, L[y][0]+1
    
    #비기는 경우
    if L[x][1] and L[y][1]>0 :
        L[x][1], L[y][1] = L[x][1]-1, L[y][1]-1
        dfs(x,y+1)
        L[x][1], L[y][1] = L[x][1]+1, L[y][1]+1

sol = []
for round in range(4):
    question = list(map(int, sys.stdin.readline().split())) 
    L = []
    for i in range(6):
        L.append([question[i*3],question[(i*3)+1],question[(i*3)+2] ])
    
    tmp = 0
    dfs(0,1)
    sol.append(tmp)
    
print(*sol)