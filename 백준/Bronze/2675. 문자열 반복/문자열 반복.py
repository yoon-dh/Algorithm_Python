num = int(input())

for i in range(num):
    a,b = map(str,input().split())
    many = int(a)
    lst = list(b)
    print(''.join([i*many for i in lst]))
