import sys

N = int(sys.stdin.readline())
cards = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
nums = map(int, sys.stdin.readline().split())

print(" ".join(map(str, [1 if num in cards else 0 for num in nums])))
