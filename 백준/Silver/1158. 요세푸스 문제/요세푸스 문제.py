import sys

N,K=sys.stdin.readline().split()
N=int(N)
K=int(K)

list = list(range(N))

idx = 0
answer = []
while list:
    idx = (idx+K-1) % len(list)
    answer.append(list[idx]+1)
    list.remove(list[idx])

print('<', end='')
for n in answer:
    print(n, end='')
    if n != answer[N-1]:
        print(', ', end='')
print('>')