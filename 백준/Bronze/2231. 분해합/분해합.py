decomposition = int(input())
answer = 0

if decomposition >= 54:
    for nums in range(decomposition-54, decomposition+1):
        if nums+sum(map(int, str(nums))) == decomposition:
            print(nums)
            break
        if nums == decomposition:
            print(0)
else:
    for nums in range(0, decomposition+1):
        if nums+sum(map(int, str(nums))) == decomposition:
            print(nums)
            break
        if nums == decomposition:
            print(0)