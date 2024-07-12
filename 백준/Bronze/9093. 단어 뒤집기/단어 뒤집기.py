import sys
from collections import deque

n = int(sys.stdin.readline())

for i in range(n):
    deq=deque(sys.stdin.readline().split())
    for i in range(len(deq)):
        reverse=''.join(reversed(deq.popleft()))
        deq.append(reverse)     
    print(' '.join(deq))