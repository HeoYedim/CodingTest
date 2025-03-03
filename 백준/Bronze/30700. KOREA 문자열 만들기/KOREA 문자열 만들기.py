S = input()
korea = "KOREA"
count = 0
idx = 0

for char in S:
    if char == korea[idx]:
        count += 1
        idx += 1
        if idx == len(korea):
            idx = 0


print(count)