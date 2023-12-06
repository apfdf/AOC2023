
lines = open("inp6.txt", "r").readlines()

time = int("".join(lines[0].removeprefix("Time:").strip().split()))
record = int("".join(lines[1].removeprefix("Distance:").strip().split()))

ways = 0
for n in range(time+1):
    if n * (time - n) > record:
        ways += 1

print(ways)
