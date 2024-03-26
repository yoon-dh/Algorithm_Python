
n=int(input())
arr=[]
lst=[]
for i in range(n):
    a=list(map(int,input().split()))
    for j in range(len(a)):
        if a[j]==5 or a[j]==2:
            lst.append([i,j])       
    arr.append(a)

x=((lst[0][0]-lst[1][0])**2+(lst[0][1]-lst[1][1])**2)**0.5
if x>=5:
    lst.sort()
    x,y=min(lst[0][1],lst[1][1]),max(lst[0][1],lst[1][1])
    cnt=0
    for i in range(lst[0][0],lst[1][0]+1):
        for j in range(x,y+1): 
            if arr[i][j]==1:
                cnt+=1

    if cnt>=3:  print(1)
    else: print(0)
    
else: print(0)
