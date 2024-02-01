import math
import sys
input = sys.stdin.readline

def segment_tree(node,start,end):
    if start == end:
        tree_min[node] = lst[start]
        return tree_min[node]
    mid = (start + end) //2
    tree_min[node] = min(segment_tree(node*2,start,mid), segment_tree(node*2+1,mid+1,end))
    return tree_min[node]

def min_find(node,start,end,left,right):
    if start > right or end < left: return 1000000001
    if left <= start and end <= right: return tree_min[node]
    mid = (start + end) // 2
    return min(min_find(node*2,start,mid,left,right),min_find(node*2+1,mid+1,end,left,right))

# ======================================

n,m = map(int,input().split())

tree_height = int(math.ceil(math.log2(n)))
tree_size = 1 << (tree_height + 1)
tree_min = [0] * tree_size
lst = [int(input()) for _ in range(n)]

segment_tree(1,0,n-1)

for _ in range(m):
    a,b = map(int,input().split())
    print(min_find(1,0,n-1,a-1,b-1))

