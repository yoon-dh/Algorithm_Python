def search(l, r):
    while abs(r - l) > 1e-9:
        l_3 = (2 * l + r) / 3
        r_3 = (l + 2 * r) / 3
        if distance_check(l_3) > distance_check(r_3):
            l = l_3
        else:
            r = r_3
    return distance_check(l)


def distance_check(t):
    mx = ax * t + bx * (1 - t)
    my = ay * t + by * (1 - t)
    kx = cx * t + dx * (1 - t)
    ky = cy * t + dy * (1 - t)
    return ((kx - mx) ** 2 + (ky - my) ** 2) ** 0.5

# ================================================

ax, ay, bx, by, cx, cy, dx, dy = map(int, input().split())
print("%.16f" % search(0, 1))