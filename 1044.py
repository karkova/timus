import sys
import math


def calc():
    n = int(sys.stdin.readline())
    n = n / 2
    max_n = int(math.pow(10, n))
    sum_d = {}
    digits = []
    for i in range(n):
        digits.append(0)

    for i in range(max_n):
        for j in range(n):
            digits[j] = i % 10
            i = i / 10
        s = sum(digits)
        if s in sum_d.keys():
            sum_d[s] = sum_d[s] + 1
        else:
            sum_d[s] = 1
    r = 0
    for v in sum_d.values():
        r = r + v * v

    print(r)


if __name__ == '__main__':
    calc()