def main():
    posled = []
    N = int(input())
    for i in range(N):
        posled.append(float(input()))

    print("{:.19e}".format(sum(posled)))


if __name__ == '__main__':
    main()