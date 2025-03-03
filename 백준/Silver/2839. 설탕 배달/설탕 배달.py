N = int(input())
five = N // 5
three = 0

while five >= 0:
    remain = N - (five * 5)
    if remain % 3 == 0:
        three = remain // 3
        print(five + three)
        break
    five -= 1
else:
    print(-1)