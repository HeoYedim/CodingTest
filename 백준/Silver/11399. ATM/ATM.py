import sys
input = sys.stdin.readline

N = int(input())
line = list(map(int,input().split()))

wating = 0
result = 0

line.sort()

for t in line:
    wating += t
    result += wating

print(result)