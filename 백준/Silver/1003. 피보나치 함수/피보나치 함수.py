import sys
input = sys.stdin.readline

T = int(input())
test_cases = [int(input()) for _ in range(T)]
result = []

for case in test_cases:
    if case == 0:
        result.append("1 0")
    else:
        zero_cnt = 1
        one_cnt = 0

        for _ in range(case):
            zero_cnt, one_cnt = one_cnt, zero_cnt + one_cnt

        result.append(f"{zero_cnt} {one_cnt}")

print("\n".join(result))