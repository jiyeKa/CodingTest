import sys

n = int(sys.stdin.readline())

for i in range(n):
    str=sys.stdin.readline().strip()
    
    stack=[]
    isTrue=True
    for char in str:
        if char=='(':
            stack.append(str)
        else:
            if not stack:
                isTrue=False
                break
            else:
                stack.pop()

    if not stack and isTrue:
        print("YES")
    else:
        print("NO")