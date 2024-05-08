N = int(input())
M = int(input())
material = list(map(int, input().split()))

left, right = 0, N-1
count = 0
material.sort()

while left < right:
    mix = material[left] + material[right]
    if mix == M:
        count += 1
        left += 1
        right -= 1
    elif mix < M:
        left += 1
    else:
        right -= 1
        
print(count)