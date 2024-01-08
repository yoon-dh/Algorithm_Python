n = int(input())
dict = {}
for _ in range(n):
    x1,y1 = map(int,input().split())
    dict[x1]=y1

sort_xy = sorted(dict.items(),key=lambda x:x[0])

x = []
y = []
for i,j in sort_xy:
    x.append(i)
    y.append(j)

# 높이가 가장 높은 기둥 찾고 그 기둥 기준 왼쪽은 오름차순 , 오른쪽은 내림차순
max_y = y.index(max(y))

x_sort = []
y_sort = []
x_sort_reverse = []
y_sort_reverse = []
start = 0
for i in range(0,max_y+1):
    if start <= y[i]:
        y_sort.append(y[i])
        x_sort.append(x[i])
        start = y[i]


reverse_start = 0
for i in range(len(y)-1,max_y-1,-1):
    if reverse_start <= y[i]:
        y_sort_reverse.append(y[i])
        x_sort_reverse.append(x[i])
        reverse_start = y[i]

x_sort_reverse.reverse()
y_sort_reverse.reverse()


Sum = 0
for i in range(len(x_sort)-1):
    Sum += (x_sort[i+1] - x_sort[i]) * y_sort[i]

for i in range(len(x_sort_reverse)-1):
    Sum += (x_sort_reverse[i+1] - x_sort_reverse[i]) * y_sort_reverse[i+1]

print(Sum + y_sort[-1])