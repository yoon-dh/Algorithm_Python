a = input()
b = a.split(' ')

num = 0
for i in range(len(b)):
    if b[i].isalpha() == True:
        num += 1

print(num)
