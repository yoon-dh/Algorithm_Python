lst = [int(input()) for _ in range(3)]
SET = set(lst)

if len(SET) == 3 and sum(lst) == 180: print("Scalene")
elif len(SET) == 2 and sum(lst) == 180: print("Isosceles")
elif len(SET) == 1 and sum(lst) == 180: print("Equilateral")
else: print("Error")