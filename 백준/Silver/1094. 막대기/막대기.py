import sys

X = int(sys.stdin.readline())

sticks = [64, 32, 16, 8, 4, 2, 1]
count = 0

for stick in sticks:
    if X >= stick:
        X -= stick
        count += 1
        
    if X == 0:
        break

print(count)