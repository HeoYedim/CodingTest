import sys
input = sys.stdin.readline

N = int(input())
files = [input().rstrip().split(".") for _ in range(N)]
answer = {}

for file in files:
    if file[1] not in answer:
        answer[file[1]] = 0

    answer[file[1]] += 1

for key in sorted(answer):
    print(key, answer[key])