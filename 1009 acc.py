def f(n, k):
    if n == 1:
        return k - 1
    elif n == 2:
        return (f(1, k) + 1) * (k - 1)
    else:
        return (f(n - 1, k) + f(n - 2, k)) * (k - 1)


def main():
    n = int(input())
    k = int(input())
    print (f(n, k))


if __name__ == '__main__':
    main()