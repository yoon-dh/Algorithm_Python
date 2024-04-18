n = int(input())
X_lst, Y_lst = [], []
for _ in range(n):
    x, y = map(int, input().split())
    X_lst.append(x)
    Y_lst.append(y)
print((max(X_lst) - min(X_lst)) * (max(Y_lst) - min(Y_lst)))