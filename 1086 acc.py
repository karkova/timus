def isPrime(n):
    if n == 1:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


k = int(input())
b = []
i = 0
while i < k:
    b.append(int(input()))
    i += 1
last = max(b)
primes = [0] * last
i = num = 0
while primes[last-1] == 0:
    if isPrime(num):
        primes[i] = num
        i += 1
    num += 1

for i in range(0, k):
    b[i] = primes[b[i]-1]
    print(b[i])