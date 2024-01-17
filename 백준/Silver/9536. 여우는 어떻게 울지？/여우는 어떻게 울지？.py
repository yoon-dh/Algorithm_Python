from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    fox = []
    sound = deque(list(input().split()))
    sound_set = set()
    while True:
        not_fox = input().rstrip()
        if not_fox == 'what does the fox say?':
            while sound:
                S = sound.popleft()
                if S not in sound_set:
                    fox.append(S)
            print(*fox)
            break

        not_fox_lst = not_fox.split()
        sound_set.add(not_fox_lst[2])