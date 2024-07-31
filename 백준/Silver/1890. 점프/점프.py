import sys

n=int(sys.stdin.readline())
map=[list(map(int, sys.stdin.readline().split()))for _ in range(n)]

dp=[[0 for _ in range(n)]for _ in range(n)]
dp[0][0]=1


for i in range(n):
    for j in range(n):
        if map[i][j] != 0 and dp[i][j] !=0:
            if i + map[i][j]<n:
                dp[i+map[i][j]][j] += dp[i][j]
            if j + map[i][j]<n:
                dp[i][j+map[i][j]] += dp[i][j]
print(dp[-1][-1])