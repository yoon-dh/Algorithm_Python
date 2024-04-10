import sys
input = sys.stdin.readline

def check(a,b,c):
    if c ** 2 == a ** 2 + b ** 2: return print("right")
    else: return print("wrong")

while True:
    arr = sorted(map(int,input().split()))
    if arr == [0,0,0]: break
    check(arr[0],arr[1],arr[2])

