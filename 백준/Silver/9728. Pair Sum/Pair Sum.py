T = int(input()) # 테스트케이스
for test_num in range(T):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split())) # 리스트

    left = 0
    right = N-1
    result = 0

    while left < right:
        if N_list[left] + N_list[right] == M:
            result += 1
            left += 1
        if N_list[left] + N_list[right] < M:
            left += 1
        if N_list[left] + N_list[right] > M:
            right -= 1

    print("Case #%d: %d" %(test_num + 1, result))