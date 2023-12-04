
lines = open("inp4.txt", "r").readlines()

copies = [1 for _ in range(len(lines))]

for i in range(len(lines)):

    # parsing input
    line = lines[i][9 : len(lines[i])].strip()
    winning_r, nums_r = line.split("|")
    winning = list(map(int, winning_r.split()))
    nums = list(map(int, nums_r.split()))

    winning_amount = 0
    for num in nums:
        if num in winning:
            winning_amount += 1

    for p in range(i+1, i+1 + winning_amount):
        copies[p] += copies[i]

print(sum(copies))
