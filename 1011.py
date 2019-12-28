def check(p, q):
    i = 1

    while True:
        if int(q * i / 100 - 0.000001) - int(p * i / 100 + 0.000001) > 0:
            return i
            break
        i += 1


def main():
    p, q = map(float, input().split())
    print(check(p, q))


if __name__ == '__main__':
    main()
