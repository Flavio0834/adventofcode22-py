res = 0

while True:
    try:
        a, b = input().split(",")
        a1, a2 = map(int, a.split("-"))
        b1, b2 = map(int, b.split("-"))
        a = range(a1, a2 + 1)
        b = range(b1, b2 + 1)
        if (a[0] in b or a[-1] in b) or (b[0] in a or b[-1] in a):
            res += 1
        continue
    except:
        break

print(res)
