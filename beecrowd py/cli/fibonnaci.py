N = int(input())

if N == 0:
    print()
else:
    a, b = 0, 1
    r = ""
    for i in range(N):
        if i > 0:
            r += " "
        r += str(a)
        a, b = b, a + b
print(r)