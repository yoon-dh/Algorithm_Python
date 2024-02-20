area = [0, 1, 3]

n = int(input())
for i in range(3, n+1):
    area.append(area[i-1] + 2 * area[i-2])

print(area[n] % 10007)