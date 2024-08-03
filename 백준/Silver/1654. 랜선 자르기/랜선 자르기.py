import sys

K, N = map(int, sys.stdin.readline().split())
arr = []
for _ in range(K):
    arr.append(int(sys.stdin.readline()))
result = 0
start = 1
end = max(arr)
while start<=end:
    mid=(start+end)//2
    count=0
    for i in arr:
        count += (i//mid)
    if count >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)