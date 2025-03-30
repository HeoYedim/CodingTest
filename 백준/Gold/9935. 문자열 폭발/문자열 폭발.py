import sys
input = sys.stdin.readline

check_string = input().strip()
bomb = input().strip()
result = []

for s in check_string:
    result.append(s)
    if ''.join(result[-len(bomb):]) == bomb:
        del result[-len(bomb):]
            
print(''.join(result) if result else "FRULA")