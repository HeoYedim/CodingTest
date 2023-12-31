num = int(input())
num_list = [int(input()) for _ in range(num)]
num_list.sort()

for i in range(len(num_list)):
    print(num_list[i])