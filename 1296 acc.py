def sum(arr):
    kek = 0
    max = 0
    for i in range (0, n):
        max = max + arr[i]
        if kek < max:
            kek = max

        if max < 0:
            max = 0
    return kek

n = int(input())
list = [0]*n
for i in range (n):
    list[i] = int(input())

print(sum(list))