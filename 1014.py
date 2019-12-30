import math

def get_factors(n):
    f = {}
    i = 9
    while i > 1:
        if n % i == 0:
            f[i] = 0
            while n % i == 0:
                f[i] = f[i] + 1
                n = n / i
        i = i - 1

    if n != 1:
        f[n] = 1

    return f

def get_result(n):
    if n == 0:
        return 10
    elif n >= 1 and n <= 9:
        return n
    else:
        f = get_factors(n)
        r = ''
        keys = f.keys()
        keys.sort()
        for k in keys:
            if k > 9:
                return -1
            r = r + str(k) * f[k]
        return int(r)

def main():
    n = int(input())
    r = get_result(n)
    print(r)

if __name__ == '__main__':
    main()