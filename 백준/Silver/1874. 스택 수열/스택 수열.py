n = int(input())
sequnce = [int(input()) for _ in range(n)]
stack = []
operation = []
idx = 1
valid = True

for num in sequnce:
    while idx <= num:
        stack.append(idx)
        operation.append('+')
        idx += 1

    if stack[-1] == num:
        stack.pop()
        operation.append('-')
    else:
        valid = False
        break

print('\n'.join(operation) if valid else "NO")