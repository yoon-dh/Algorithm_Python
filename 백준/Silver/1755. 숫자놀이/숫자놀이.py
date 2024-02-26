import sys
input = sys.stdin.readline

num_dict = {'1':'one', '2':'two', '3':'three', '4': 'four', '5':'five',
            '6':'six', '7': 'seven', '8':'eight', '9':'nine', '0':'zero'}

alpha_dict = {'one':'1', 'two':'2', 'three':'3','four':'4', 'five':'5',
              'six':'6','seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'}

N,M = map(int,input().rstrip().split())
num_list = [list(str(i)) for i in range(N,M+1)]

ans_list = []
for i in num_list:
    temp = ''
    for k in i:
        temp += num_dict[k] + ' '
    ans_list.append(temp.rstrip())

ans_list.sort()

ANS = []

for i in ans_list:
    temp_lst = i.split()
    result = ''
    for k in temp_lst:
        result += alpha_dict[k]
    ANS.append(int(result))

for i in range(1,len(ANS)+1):
    if i % 10 == 0: print(ANS[i-1],end='\n')
    else: print(ANS[i-1],end=' ')


