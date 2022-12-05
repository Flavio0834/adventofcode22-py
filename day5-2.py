res = 0

tours = [
    ["B", "W", "N"],
    ["L", "Z", "S", "P", "T", "D", "M", "B"],
    ["Q", "H", "Z", "W", "R"],
    ["W", "D", "V", "J", "Z", "R"],
    ["S", "H", "M", "B"],
    ["L", "G", "N", "J", "H", "V", "P", "B"],
    ["J", "Q", "Z", "F", "H", "D", "L", "S"],
    ["W", "S", "F", "J", "G", "Q", "B"],
    ["Z", "W", "M", "S", "C", "D", "J"],
]

while True:
    try:
        a = input().split()
        k = int(a[1])
        i, j = int(a[3]), int(a[5])

        x = tours[i - 1][-k:]
        tours[i - 1] = tours[i - 1][:-k]
        tours[j - 1] = tours[j - 1] + x
        continue
    except:
        break

print("".join(k[-1] for k in tours))
print(tours)
