a = int(input())
b = input()

b_int = [int(i) for i in b]
print(f'{a*b_int[2]}\n{a*b_int[1]}\n{a*b_int[0]}\n{a*b_int[2]+a*b_int[1]*10+a*b_int[0]*100}')