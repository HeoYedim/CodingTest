num = int(input())
xy_list = []

for _ in range(num):
    [x, y] = map(int, input().split())
    xy_list.append([x, y])
xy_list.sort()

for xy in xy_list:
    print(xy[0], xy[1])