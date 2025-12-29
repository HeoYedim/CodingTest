import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    x = input().split()

    if x[0] == "1":
        stack.append(int(x[1]))
    elif x[0] == "2":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif x[0] == "3":
        print(len(stack))
    elif x[0] == "4":
        print(0 if stack else 1)
    elif x[0] == "5":
        if stack:
            print(stack[-1])
        else:
            print(-1)