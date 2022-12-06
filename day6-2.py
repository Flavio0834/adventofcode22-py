a = input()
i = 0
found = False
found_l = [False for z in range(14)]


while not found:
    for j in range(14):
        if not (a[j] in a[:j] or a[j] in a[j + 1 : 4]):
            found_l[j] = True
    if found_l == [True for z in range(14)]:
        found = True
        break
    else:
        i += 1
        a = a[1:]
        found_l = [False for z in range(14)]

print(i)
