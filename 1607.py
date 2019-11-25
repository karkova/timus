def main():
    a, b, c, d = map(int, input().split())
    kek = 0

    if a > c:
        print(a)
    elif a == c:
        print(a)
    else:
        while kek != 1:
            a += b
            if c - d < a:
                kek = 1
                print(a)
            else:
                c -= d
                if a + b > c:
                    kek = 1
                    print(c)

if __name__ == '__main__':
    main();