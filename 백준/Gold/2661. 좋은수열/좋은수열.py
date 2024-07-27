N=int(input())
arr=[]

def dfs(index):
    for i in range(1,(index//2)+1):
        if arr[-i:]==arr[-2*i:-i]:
            return -1
    if index==N:
        for n in arr:
            print(n,end="")
        print()
        return 0
    for i in range(1,4):
        arr.append(i)
        if dfs(index+1)==0:
            return 0
        arr.pop()

dfs(0)