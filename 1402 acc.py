import math


def main():
    n = int(input())
    c = int(0)

    for i in range(2, n + 1):
        tmp_c = int(math.factorial(n) / (math.factorial(n - i)))
        c = c + tmp_c

    print(c)


if __name__ == '__main__':
    main()