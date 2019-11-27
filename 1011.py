import math


def check(p, q):
    i = 2
    for i in range(10000):
        if math.floor(i * (q / 100)) > math.floor(i * (p / 100)):
            return i
            break
        i += 1


def main():
    p = float(input())
    q = float(input())
    print(check(p, q))


if __name__ == '__main__':
    main()
