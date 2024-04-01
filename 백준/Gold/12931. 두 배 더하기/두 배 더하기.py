import sys
input = sys.stdin.readline

def check_num():
    global odd, even

    temp = []
    for i in even:
        if i % 2 != 0: odd.append(i)
        else: temp.append(i)

    even = temp
    if len(odd): return False
    else: return True

def divede_all():
    global even
    even = list(map(lambda x: x // 2,even))

def minus_one():
    global odd,even
    even.append(odd.pop() - 1)

# ==========================================

n = int(input())
B = list(map(int,input().split()))

odd = []
even = []

for i in B:
    if i % 2 == 0: even.append(i)
    else: odd.append(i)

cnt = 0
while True:
    if sum(even) != 0 or sum(odd) != 0:
        isAllTwo = check_num()
        if isAllTwo: divede_all()
        else: minus_one()
        cnt += 1
    else:
        print(cnt)
        break