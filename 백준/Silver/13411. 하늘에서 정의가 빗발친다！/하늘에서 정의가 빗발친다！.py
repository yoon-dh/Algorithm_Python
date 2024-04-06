import sys
input = sys.stdin.readline

n=int(input())
arr=[]

for i in range(1,n+1):
    x,y,v=map(int,input().split())
    dist = (x ** 2 + y ** 2) ** 0.5
    arr.append((dist / v, i))

arr.sort(key=lambda x:(x[0],x[1]))
for i in range(n):
    print(arr[i][1])
