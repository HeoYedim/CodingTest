import sys

N = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(N)]

for i in sorted(num):
    print(i)