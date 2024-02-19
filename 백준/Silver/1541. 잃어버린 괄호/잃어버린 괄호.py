import sys

num_list = list(map(str, sys.stdin.readline().rstrip().split('-')))
result = sum(list(map(int,num_list[0].split('+'))))

for i in range(1, len(num_list)):
    result -= sum(list(map(int,num_list[i].split('+'))))

print(result)