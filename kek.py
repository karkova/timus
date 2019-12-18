def a(n):
    if n <=0:
        return 0
    if n == 1:
        return 1
    if n%2 == 0:
        return a(n/2)
    i = (n-1)/2
    return a(i)+a(i+1)

def gena(n):
    for i in range(n+1):
        yield a(i)

def findmax(nn):
    for n in nn:
        yield max(gena(n))

def out(nn):
    for m in findmax(nn):
        print(m)

def main2():
    out([5,10])
