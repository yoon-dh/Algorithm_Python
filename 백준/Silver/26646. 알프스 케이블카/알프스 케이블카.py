import sys
input = sys.stdin.readline

N=int(input())
n = list(map(int,input().split()))
line = abs(n[0]-n[1])**2 + (n[0]+n[1])**2
for x in range(1,N-1):
    line = min(line+abs(n[x]-n[x+1])**2+(n[x]+n[x+1])**2,abs(n[0]-n[x+1])**2 + ((sum(n[0:x+2])*2-n[0]-n[x+1])**2))

print(line)