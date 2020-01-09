n, k = map(int, input().split())
s = list(input().split())
iterator = 0
if n % k:
    out = ["" for i in range(n//k+1)]
else:
    out = ["" for i in range(n // k)]
for i in range(0, len(s)):
    if len(s[i]) == 1:
        s[i] = "   " + s[i]
    elif len(s[i]) == 2:
        s[i] = "  " + s[i]
    elif len(s[i]) == 3:
        s[i] = " " + s[i]
    else:
        s[i] = "" + s[i]
for i in range(0, len(s)):
    if iterator == len(out):
        iterator = 0
    out[iterator] = out[iterator] + s[i]
    iterator += 1
for i in range (0, len(out)):
    print(out[i])