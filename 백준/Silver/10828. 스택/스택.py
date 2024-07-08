import sys

num = int(sys.stdin.readline())
stack=[]
top=-1
for i in range(num):
    str=sys.stdin.readline()
    str=str.split()

    if str[0]=="push":
        tmp=int(str[1])
        stack.append(tmp)
        top+=1
    elif str[0]=="pop":
        if top!=-1:
            tmp=stack[top]
            stack.pop(top)
            top-=1
        else:
            tmp=-1
        print(tmp)
    elif str[0]=="size":
        print(top+1)
    elif str[0]=="empty":
        tmp=1 if top==-1 else 0
        print(tmp)
    elif str[0]=="top":
        tmp=stack[top] if top!=-1 else -1
        print(tmp)
