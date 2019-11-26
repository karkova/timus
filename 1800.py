import math


def main():
    l, h, w = map(int, input().split())
    print(check(l, h, w))

def check(l, h, w):
  g = 9.81
  t = math.sqrt((2 * h) / g) // время падения
  f = w * t // угол поворота за падение
  N = f / (2 * math.pi) //количество оборотов

if __name__ == '__main__':
    main();
