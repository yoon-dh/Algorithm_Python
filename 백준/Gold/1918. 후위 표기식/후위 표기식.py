class Stack():
    def __init__(self):
        self.s = []

    def __str__(self):
        return str(self.s)

    def isEmpty(self):
        return len(self.s) == 0

    def size(self):
        return len(self.s)

    def clear(self):
        self.s = []

    def push(self, item):
        self.s.append(item)

    def pop(self):
        if not self.isEmpty(): return self.s.pop(-1)

    def peek(self):
        if not self.isEmpty(): return self.s[-1]


def precedence(op):
    if op == '(' or op == ')' : return 0
    elif op == '+' or op == '-': return 1
    elif op == '*' or op == '/': return 2
    else: return -1

def Infix2PostFix(expr):
    s = Stack()
    output = []

    for term in expr:
        if term in '(':
            s.push('(')
        elif term in ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(': break
                else: output.append(op)
        elif term in '+-*/':
            while not s.isEmpty():
                op = s.peek()
                if precedence(term) <= precedence(op):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)
        else:
            output.append(term)

    while not s.isEmpty():
        output.append(s.pop())

    return output


print(''.join(Infix2PostFix(input())))