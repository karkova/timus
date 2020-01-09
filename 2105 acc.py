l, ta, va, vb = map(int, input().split())
tb = ta
n = int(input())
for i in range(0, n):
    data = input().split()
    person = int(data[0])
    feed = int(data[2])
    if person == 2:
        tb -= feed
    else:
        ta -= feed

print(int((va*ta + vb*tb)/l))