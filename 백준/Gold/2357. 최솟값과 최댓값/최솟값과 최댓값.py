import sys
input = sys.stdin.readline

def segment_tree(start, end, node, tree, Min_Max):
    if start == end:
        tree[node] = G[start]
        return tree[node]
    mid = (start + end) // 2
    if Min_Max:tree[node] = min(segment_tree(start, mid, node * 2, tree, Min_Max), segment_tree(mid + 1, end, node * 2 + 1, tree, Min_Max))
    else: tree[node] = max(segment_tree(start, mid, node * 2, tree, Min_Max), segment_tree(mid + 1, end, node * 2 + 1, tree, Min_Max))
    return tree[node]


def query(start, end, node, left, right, tree, Min_Max):
    if left > end or right < start: return sys.maxsize if Min_Max else -sys.maxsize
    if left <= start and end <= right: return tree[node]

    mid = (start + end) // 2
    if Min_Max: return min(query(start, mid, node * 2, left, right, tree, Min_Max), query(mid + 1, end, node * 2 + 1, left, right, tree, Min_Max))
    else: return max(query(start, mid, node * 2, left, right, tree, Min_Max), query(mid + 1, end, node * 2 + 1, left, right, tree, Min_Max))

# =============================================================================

n, m = map(int, input().split())
G = [int(input()) for _ in range(n)]
Min_tree = [0 for _ in range(len(G) * 4)]
Max_tree = [0 for _ in range(len(G) * 4)]

segment_tree(0, n - 1, 1, Min_tree, True)
segment_tree(0, n - 1, 1, Max_tree, False)
for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(query(0, n - 1, 1, a - 1, b - 1, Min_tree, True), query(0, n - 1, 1, a - 1, b - 1, Max_tree, False))