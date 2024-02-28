E, S, M = map(int, input().split())
year = 0
e, s, m = 0, 0, 0

while True:
    if e==E and s==S and m==M:
        break
    e = e % 15 + 1
    s = s % 28 + 1
    m = m % 19 + 1
    year += 1
print(year)