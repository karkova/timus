def main():
  n = int(input())
  numbers =[]
  for i in range(0, n):
      numbers.append(int(input()))
  useless = input()
  k = int(input())
  positions = []
  for i in range(0, k):
      positions.append(int(input()))
  numbers = sorted(numbers)
  for i in range(0, k):
      print(numbers[positions[i]-1])


if __name__ == '__main__':
    main();