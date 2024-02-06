lst = list(input().split(':'))

if lst.count(''):
    while len(lst) > 8: del lst[lst.index('')]
    while len(lst) < 8: lst.insert(lst.index(''), '0000')

for i in range(8):
    if len(lst[i]) < 4: lst[i] = '0'*(4-len(lst[i])) + lst[i]

ans = ':'.join(lst)
print(ans)