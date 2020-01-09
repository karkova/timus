def main():
    t1, t2 = map(int, input().split())
    tries = map(int, input().split())
    for i in tries:
        if i != 0:
            t2 = t2 - i * 20

    if t2 >= t1:
        print('No chance.')
    else:
        print('Dirty debug :(')

if __name__ == '__main__':
    main()