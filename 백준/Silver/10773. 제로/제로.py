k = int(input())
money = [int(input()) for _ in range(k)]
total = []

for i in money:
    if i != 0:
        total.append(i)
    else:
        total.pop()
print(sum(total))