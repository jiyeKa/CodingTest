import sys

def dfs(index):
    if len(answer) == L:
        vo, co = 0, 0
        for i in range(L):
            if answer[i] in vowel:
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            print(''.join(answer))
    for i in range(index, C):
        answer.append(list[i])
        dfs(i + 1)
        answer.pop()


L, C = map(int, sys.stdin.readline().split())
list = sorted(list(sys.stdin.readline().split()))
vowel = ['a', 'i', 'o', 'u', 'e']
answer = []
dfs(0)