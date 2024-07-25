import sys

def dfs(index, sum):
    global count
    if index >= N:
        return
    sum+=list[index]
    if sum==S:
        count+=1
    dfs(index+1,sum)
    dfs(index+1,sum-list[index]) 

N,S = map(int, sys.stdin.readline().split())
list = list(map(int, sys.stdin.readline().split()))
count = 0 
visited = [False]*N 
dfs(0, 0)
print(count)