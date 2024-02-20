import sys
input = sys.stdin.readline
from collections import deque


def cal(num):
  for i in range(len(num)):
    n = int(num[len(num)-i-1],36)
    lst[n] += (35 - n) * (36 ** i)

def translate(x):
  if x == 0: return 0
  Q = deque()
  while x:
    Q.appendleft(n36[x%36])
    x //= 36
  return "".join(Q)

# ============================================================

N = int(input())

Sum = 0
lst = [0]*36
n36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(N):
  num = input().strip()
  Sum += int(num,36)
  cal(num)

lst.sort(reverse=True)
K = int(input())

for i in range(K):
  Sum += lst[i]

print(translate(Sum))