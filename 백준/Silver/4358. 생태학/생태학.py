import sys

total = 0
dictionary = dict()
while 1:
    word = sys.stdin.readline().rstrip()
    if word == '':
        break
    total += 1
    if word in dictionary: dictionary[word] += 1
    else: dictionary[word] = 1

sort_dict = dict(sorted(dictionary.items()))
for i in sort_dict:
    a = sort_dict[i]
    per = (a / total * 100)

    print("%s %.4f" % (i, per))