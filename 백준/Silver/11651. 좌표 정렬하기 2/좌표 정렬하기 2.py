num = int(input())
xy_list = []

for _ in range(num):
    xy_list.append(list(map(int, input().split())))

xy_list.sort(key = lambda x: (x[1], x[0]))

for xy in xy_list:
    print(xy[0], xy[1])