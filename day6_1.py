
lines = open("inp6.txt", "r").readlines()

times = list(map(int, lines[0].removeprefix("Time:").strip().split()))
distances = list(map(int, lines[1].removeprefix("Distance:").strip().split()))

prod = 1

for i in range(len(times)):
    
    time = times[i]
    record = distances[i]

    ways = 0

    for n in range(time+1):
        distance = (time - n) * n
        if distance > record:
            ways += 1

    prod *= ways

print(prod)
