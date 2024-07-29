import sys
n=int(sys.stdin.readline())
block=sys.stdin.readline().rstrip()

dp=[float('inf')]*n
dp[0]=0
for i in range(1,n):
    for j in range(i):
        if block[j]=="B"and block[i]=="O":
            dp[i]=min(dp[i],dp[j]+pow(i-j,2))
        elif block[j]=="O" and block[i]=="J":
            dp[i]=min(dp[i],dp[j]+pow(i-j,2))
        elif block[j]=="J" and block[i]=="B":
            dp[i]=min(dp[i],dp[j]+pow(i-j,2))
if dp[n-1]!=float('inf'):
    print(dp[n-1])
else:
    print(-1)
