def main():
    a = [0, 1]
    n = []

    for i in range(11):
        n.append(int(input()))
        if n[i] == 0:
            break

    for i in range(2,max(n) + 1):
        a.append(0)

    for j in range(len(n) - 1):
        for i in range((n[j] + 1)):
            if i % 5 == 0 and i % 2 == 0 and 2 * i + 1 >= n[j]:
                break
            elif 2 * i + 1 == n[j] and n[j] / 4 - (int(n[j] / 4)) == 0.75:
                a[2 * i] = a[i]
                a[2 * i + 1] = a[i] + a[i + 1]
                break
            elif i % 2 == 0 and 2 * i + 1 >= n[j]:
                a[2 * i] = a[i]
                a[2 * i + 1] = a[i] + a[i + 1]
                break
            elif i % 2 != 0 and 2 * i == n[j]:
                a[2 * i] = a[i]
                break
            else:
                a[2 * i] = a[i]
                a[2 * i + 1] = a[i] + a[i + 1]
        print(max(a))


if __name__ == '__main__':
    main()
