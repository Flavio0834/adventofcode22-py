letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = 0

while True:
    try:
        a, b, c = input(), input(), input()
        for letter in letters:
            if letter in a and letter in b and letter in c:
                res += letters.index(letter) + 1

        continue
    except:
        break

print(res)
