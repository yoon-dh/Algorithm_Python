n = input()
from collections import Counter

C = dict(Counter(n))

Sum = 0
ans = ''
if C.get("0") == None: print(-1)
else:
    for i in C.keys():
        Sum += int(i) * C[i]

    if Sum % 3 == 0:
       for i in sorted(C.items(),key=lambda x:x[0],reverse=True):
           ans += i[0] * i[1]
       print(ans)

    else: print(-1)