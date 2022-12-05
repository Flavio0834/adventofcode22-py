letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = 0

while True:
    try:
        a = input()
        a1, a2 = a[: len(a) // 2], a[len(a) // 2 :]
        for letter in letters:
            if letter in a1 and letter in a2:
                res += letters.index(letter) + 1

        continue
    except:
        break

print(res)
