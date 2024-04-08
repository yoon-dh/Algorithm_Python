import sys
input = sys.stdin.readline

a=list(map(int,input().split()))
b=list(map(int,input().split()))

if a[2]<b[0] or a[0]>b[2] or a[1]>b[3] or a[3]<b[1]: print('NULL')
elif (a[2]==b[0] and a[3]==b[1]) or (a[0]==b[2] and a[1]==b[3]) or (a[2]==b[0] and a[1]==b[3]) or (a[0]==b[2] and a[3]==b[1]): print('POINT')
elif a[2]==b[0] or a[0]==b[2] or a[1]==b[3] or a[3]==b[1]: print('LINE')
else: print("FACE")