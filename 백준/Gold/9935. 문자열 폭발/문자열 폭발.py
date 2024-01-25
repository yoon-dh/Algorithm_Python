import sys
input = sys.stdin.readline

S = input().rstrip()
bomb = input().rstrip()
Stack = []

for i in range(len(S)):
    Stack.append(S[i])
    if ''.join(Stack[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            Stack.pop()

if Stack: print(''.join(Stack))
else: print('FRULA')
