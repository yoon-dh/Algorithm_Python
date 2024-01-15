import sys

S = sys.stdin.readline().strip() + ' '
stack = []
result = ''
current = False
for i in S:
    if i == '<':
        current = True
        for _ in range(len(stack)):
            result += stack.pop()
    stack.append(i)

    if i == '>':
        current = False
        for _ in range(len(stack)):
            result += stack.pop(0)

    if i == ' ' and current == False:
        stack.pop()
        for _ in range(len(stack)):
            result += stack.pop()
        result += ' '
print(result)