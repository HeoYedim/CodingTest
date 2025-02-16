N, K = map(int, input().split())
cat_weights = list(map(int, input().split()))

start, end = 0, len(cat_weights)-1
cat_weights.sort() # [2, 4, 8, 11, 16]
cnt = 0

while start < end:
    if cat_weights[start] + cat_weights[end] <= K:
        cnt += 1
        start += 1
        end -= 1
    elif cat_weights[start] + cat_weights[end] > K:
        end -= 1

print(cnt)