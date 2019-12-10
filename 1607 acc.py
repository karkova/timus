def main():
    a, b, c, d = map(int, input().split())
    print(check(a,b,c,d))

def check(a,b,c,d):
    if a >= c:
        return a
    else:
        while True:
          if a + b > c:
            return c
          else:
            a += b
            if c - d < a:
                return a
            else:
                c -= d
                if a + b > c:
                    return c

if __name__ == '__main__':
    main();