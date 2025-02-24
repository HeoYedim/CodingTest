N = int(input())
K = int(input())
sensors = sorted(list(map(int, input().split()))) # [1, 3, 6, 6, 7, 9]

gaps = sorted(sensors[i + 1] - sensors[i] for i in range(N - 1)) # [0, 1, 2, 2, 3]

print(sum(gaps[:N - K]))