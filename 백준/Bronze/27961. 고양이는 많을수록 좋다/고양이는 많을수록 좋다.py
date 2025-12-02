import sys
input = sys.stdin.readline

N = int(input())

if N == 0:
    print(0)
else:
    action = 1
    cat = 1

    while cat < N:
        cat *= 2
        action += 1
    print(action)