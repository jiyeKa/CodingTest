import sys
from collections import deque

s = int(sys.stdin.readline())
q = deque()
next = deque()
sec = 0
visited = [False] * 2001
q.append((1, 0))

while True:
    if not q:
        sec += 1
        q = next
        next = deque()
    now, clipboard = q.popleft()
    visited[now] = True
    if s in [now + clipboard, now - 1]:
        print(sec + 1)
        break
    if clipboard != 0 and (now + clipboard) < 2000:
        if not visited[now + clipboard]:
            next.append((now + clipboard, clipboard))
    if now != 0:
        next.append((now, now))
        if not visited[now - 1]:
            next.append((now - 1, clipboard))