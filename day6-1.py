a = input()
i = 0
found = False
found_l = [False for z in range(4)]


while not found:
    for j in range(4):
        if not (a[j] in a[:j] or a[j] in a[j + 1 : 4]):
            found_l[j] = True
    if found_l == [True for z in range(4)]:
        found = True
        break
    else:
        i += 1
        a = a[1:]
        found_l = [False for z in range(4)]

print(i)
print(a[i : i + 4], a[i - 1 : i + 3], a[i + 1 : i + 5])
