score = 0

while True:
    try:
        x, y = input().split()
        turn = 0
        if y == "X":
            turn += 1
        elif y == "Y":
            turn += 2
        elif y == "Z":
            turn += 3

        if (
            (x == "A" and y == "X")
            or (x == "B" and y == "Y")
            or (x == "C" and y == "Z")
        ):
            turn += 3
        elif (
            (y == "X" and x == "B")
            or (y == "Y" and x == "C")
            or (y == "Z" and x == "A")
        ):
            pass
        else:
            turn += 6

        score += turn
    except:
        break

print(score)
