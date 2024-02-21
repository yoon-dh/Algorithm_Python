ans = 1
while True:
  stack = []
  cnt = 0
  S = input()

  if '-' in S:
    break

  for i in S:
    if i == "{": stack.append(i)
    else:
      if stack: stack.pop()
      else:
        cnt += 1
        stack.append('{')

  cnt += len(stack) // 2

  print(f'{ans}. {cnt}')
  ans += 1