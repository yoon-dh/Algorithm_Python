from math import sqrt
d,h,w = map(int,input().split())
r = d/sqrt(h**2+w**2)
print(int(h*r),int(w*r))