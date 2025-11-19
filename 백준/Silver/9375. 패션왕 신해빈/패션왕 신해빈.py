import sys
from collections import Counter
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    if n > 0:
        wear_type_cnt = Counter(input().split()[1] for _ in range(n))
    else:
        wear_type_cnt = {}

    cnt = 1

    for count in wear_type_cnt.values():
        cnt *= (count + 1)

    print(cnt - 1)