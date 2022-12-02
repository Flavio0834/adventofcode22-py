score = 0

while True:
    try:
        x, y = input().split()
        turn = 0

        if y == "X":
            if x == "A":
                turn += 3
            elif x == "B":
                turn += 1
            else:
                turn += 2

        elif y == "Y":
            if x == "A":
                turn += 4
            elif x == "B":
                turn += 5
            else:
                turn += 6

        else:
            if x == "A":
                turn += 8
            elif x == "B":
                turn += 9
            else:
                turn += 7

        score += turn
    except:
        break

print(score)
