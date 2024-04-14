import sys
input = sys.stdin.readline

def check(n1,n2):
    return abs((n2[0]-n1[0])**2+abs(n2[1]-n1[1])**2)

# ================================================

t=int(input())
arr=[]
tmp=0

for _ in range(t):
    arr = []
    for _ in range(4):
        a,b=map(int,input().split())
        arr.append([a,b])

    arr=sorted(arr)

    for dot in arr:
        if dot==[0,0]:
            tmp+=1
    if tmp==4:
        print(0)
        tmp=0
    elif check(arr[0],arr[1])==check(arr[0],arr[2])==check(arr[1],arr[3]) and check(arr[1],arr[2])==check(arr[0],arr[3]): print(1)
    else: print(0)