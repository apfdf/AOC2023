
digit_chars = "1234567890"

lines = open("inp5.txt", "r").readlines()

seeds = list(map(int, lines[0].removeprefix("seeds: ").split()))

lowest_loc = 10**10

maps = []
current_map = []

for i in range(len(lines)):
    line = lines[i]
    if line[0] in digit_chars:
        current_map.append(list(map(int, line.split())))
    if len(current_map) != 0 and (line[0] not in digit_chars or i == len(lines)-1):
        maps.append(current_map)
        current_map = []

print(len(maps))

for seed in seeds:
    
    p = seed
    for i in range(len(maps)):
        
        print(seed, p)

        current_map = maps[i]
        
        for j in range(len(current_map)):
            
            dest_begin = current_map[j][0]
            source_begin = current_map[j][1]
            length = current_map[j][2]

            if p >= source_begin and p <= source_begin + length:
                p = p - source_begin + dest_begin
                break


    if p < lowest_loc:
        lowest_loc = p

print(lowest_loc)
