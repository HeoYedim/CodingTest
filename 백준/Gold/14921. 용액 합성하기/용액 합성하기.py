N = int(input())
N_list = list(map(int, input().split()))

left, right = 0, N-1
mix = N_list[left] + N_list[right]

while left < right:
    tmp = N_list[left] + N_list[right]
    if abs(tmp) < abs(mix):
        mix = tmp
    
    if tmp < 0:
        left += 1
    else:
        right -= 1

print(mix)