
lines = open("inp2.txt", "r").readlines()

s = 0

for i in range(len(lines)):

    line = lines[i]
    line = line.removeprefix("Game " + str(i+1) + ": ")

    possible = True

    subsets = line.split(";")

    for subset in subsets:

        amounts = {
            "red" : 0,
            "green" : 0,
            "blue" : 0
        }

        groups = subset.split(", ")

        print(groups)

        for group in groups:

            amount, color = group.split()
            amount = int(amount)

            amounts[color] += amount

        if amounts["red"] > 12 or amounts["green"] > 13 or amounts["blue"] > 14:
            possible = False
            break
    
    if possible:
        s += i + 1

print(s)
