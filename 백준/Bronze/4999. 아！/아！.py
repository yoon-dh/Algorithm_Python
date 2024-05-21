from collections import Counter

me = Counter(input())
doc = Counter(input())

if me['a'] >= doc['a'] and me['h'] >= doc['h']: print("go")
else: print("no")