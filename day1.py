L = []
x = 0
while True:
    try:
        a = input()
        if a != "":
            x += int(a)
        else:
            L.append(x)
            x = 0
            continue
    except:
        break

print(L)
print(max(L))

print(sum(sorted(L)[::-1][:3]))
