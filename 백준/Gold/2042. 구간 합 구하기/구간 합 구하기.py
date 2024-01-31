import sys
input = sys.stdin.readline

def segment_tree(node, start, end):
    if start == end:
        tree[node] = lst[start]
        return tree[node]
    else:
        tree[node] = segment_tree(node * 2, start, (start + end) // 2) + segment_tree(node * 2 + 1, (start + end) // 2 + 1, end)
        return tree[node]

def section_sum(node, start, end, left, right):
    if left > end or right < start: return 0
    if left <= start and end <= right: return tree[node]
    return section_sum(node * 2, start, (start + end) // 2, left, right) + section_sum(node * 2 + 1, (start + end) // 2 + 1, end,
                                                                             left, right)


def update(node, start, end, index, diff):
    if index < start or index > end: return

    tree[node] += diff

    if start != end:
        update(node * 2, start, (start + end) // 2, index, diff)
        update(node * 2 + 1, (start + end) // 2 + 1, end, index, diff)

# ========================================================================

n, m, k = map(int, input().rstrip().split())

lst = [int(input().rstrip()) for _ in range(n)]
tree = [0] * 3000000

segment_tree(1, 0, n - 1)

for _ in range(m + k):
    a, b, c = map(int, input().rstrip().split())

    if a == 1:
        b = b - 1
        diff = c - lst[b]
        lst[b] = c
        update(1, 0, n - 1, b, diff)
    elif a == 2:
        print(section_sum(1, 0, n - 1, b - 1, c - 1))