import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    applicants = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

    applicants.sort()

    cnt = 1
    min_interview_rank = applicants[0][1]

    for i in range(1, n):
        if applicants[i][1] < min_interview_rank:
            cnt += 1
            min_interview_rank = applicants[i][1]

    print(cnt)