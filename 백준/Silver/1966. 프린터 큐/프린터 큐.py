import sys
from collections import deque

n = int(sys.stdin.readline())

for i in range(n):
    N,M=map(int,sys.stdin.readline().split())
    importance=deque(sys.stdin.readline().split())
    count=0
    while importance:
        if importance[0]>=max(importance):
            count+=1
            if M==0:
                print(count)
                break
            importance.popleft()
            M-=1
        else:
            importance.append(importance.popleft())
            M=len(importance)-1 if M==0 else M-1 