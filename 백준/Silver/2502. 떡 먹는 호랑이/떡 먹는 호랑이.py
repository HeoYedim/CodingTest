import sys
input = sys.stdin.readline

def fibo(n):
    fib = [0] * (n + 1)
    fib[0], fib[1] = 0, 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib

D, K = map(int, input().split())

fib = fibo(D)
A = fib[D - 2]
B = fib[D - 1]

for a in range(1, K):
    remain = K - A * a
    if remain % B == 0:
        b = remain // B
        if b >= 1:
            print(a)
            print(b)
            break