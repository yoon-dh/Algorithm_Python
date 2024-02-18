def check(a, b):
  cnt = 0
  for i in range(min(len(a), len(b))):
    if a[i] == b[i]:
      cnt += 1
    else:
      break
  return cnt


n = int(input())
a = [input() for _ in range(n)]
b = sorted(list(enumerate(a)), key=lambda x: x[1])

lst = [0] * (n + 1)
maxlength = 0

for i in range(n - 1):
  tmp = check(b[i][1], b[i + 1][1])
  maxlength = max(maxlength, tmp)
  lst[b[i][0]] = max(lst[b[i][0]], tmp)
  lst[b[i + 1][0]] = max(lst[b[i + 1][0]], tmp)

first = 0
for i in range(n):
  if first == 0:
    if lst[i] == max(lst):
      first = a[i]
      print(first)
      pre = a[i][:maxlength]
  else:
    if lst[i] == max(lst) and a[i][:maxlength] == pre:
      print(a[i])
      break