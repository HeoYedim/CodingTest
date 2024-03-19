n = int(input())
ps_list = [str(input()) for _ in range(n)]

for ps in ps_list:
    stack = []
    valid = True
    for p in ps:
        if p == "(":
            stack.append(p)
        else:
            if not stack:
                valid = False
                break
            stack.pop()
    print("YES" if valid and not stack else "NO")