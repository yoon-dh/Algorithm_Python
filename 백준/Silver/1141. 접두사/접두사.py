import sys
input = sys.stdin.readline

n = int(input())
words = sorted([input().rstrip() for _ in range(n)], key=len)

ans = 0

for i in range(n):
    f = False
    for j in range(i + 1, n):
        if words[i] == words[j][0:len(words[i])]:
            f = True
            break

    if not f: ans += 1

print(ans)