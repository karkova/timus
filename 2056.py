def main():
    n = int(input())
    m = []
    for i in range(n):
        m.append(int(input()))
    if 3 in m:
        print("None")
    elif sum(m) / 5 == n:
        print("Named")
    elif sum(m) / len(m) >= 4.5:
        print("High")
    elif sum(m) / len(m) < 4.5:
        if 3 not in m:
            print("Common")

if __name__ == '__main__':
    main()
