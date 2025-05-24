import sys
input = sys.stdin.readline

N = int(input())
xy_list = [tuple(map(int, input().split())) for _ in range(N)]

xy_list.sort(key = lambda x: (x[1], x[0]))

for xy in xy_list:
    print(xy[0], xy[1])