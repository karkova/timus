def sum(arr):
    k = 0
    max = 0
    for i in range (0,len(arr)):
        max = max + arr[i]
        if k < max:
            k = max

        if max < 0:
            max = 0
    return k

n = (int)(input())
list = [None]*n
for i in  range (n):
    list[i] = (int)(input())

print(sum(list))