
lines = open("inp2.txt", "r").readlines()

s = 0

for i in range(len(lines)):

    line = lines[i]
    line = line.removeprefix("Game " + str(i+1) + ": ")

    min_amounts = {
        "red" : 0,
        "green" : 0,
        "blue" : 0
    }

    subsets = line.split(";")

    for subset in subsets:

        groups = subset.split(", ")

        amounts = {
            "red" : 0,
            "green" : 0,
            "blue" : 0
        }

        for group in groups:

            amount, color = group.split()
            amount = int(amount)

            amounts[color] += amount
        
        for color in ["red", "green", "blue"]:
            if amounts[color] > min_amounts[color]:
                min_amounts[color] = amounts[color]
    
    s += min_amounts["red"] * min_amounts["green"] * min_amounts["blue"]

print(s)
