x, y, c = map(float, input().split())
s, e = 0, min(x, y)


def calc(mid):
    a = (x**2-mid**2) ** 0.5
    b = (y**2-mid**2) ** 0.5
    return a*b/(a+b)


ans = 0
while e-s > 1e-6:
    mid = (s+e)/2
    if calc(mid) >= c:
        ans = mid
        s = mid
    else: e = mid

print("{}".format(round(ans, 4)))