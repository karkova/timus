import math

def main():
    l, h, w = map(int, input().split())
    print(check(l, h, w))

def check(l, h, w):
    f = math.sqrt(h/l)
    if math.copysign(1, math.sqrt(h/l)) == 1:
        return("butter")
    elif math.copysign(1, math.sqrt(h/l)) == -1:
        return("bread")

if __name__ == '__main__':
    main();
