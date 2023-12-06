
#dålig brute-force lösning som tar alldelles för lång tid

#idé gör ett sätt att reducera ett några intervall till några intervall med minst antal som har samma union

def update_intervals(intervals):
    
    should_update = True
    while should_update:
        
        should_update = False

        for i in range(len(intervals)):
            for j in range(len(intervals)):
        
                if i == j:
                    continue
                
                lo1 = intervals[i][0]
                hi1 = intervals[i][1]

                lo2 = intervals[j][0]
                hi2 = intervals[j][1]
        
                if (lo1 >= lo2 and lo1 <= hi2) or (hi1 >= lo2 and hi1 <= hi2):
                    del intervals[j]
                    intervals[i] = (min(lo1, lo2), max(hi1, hi2))
                    should_update = True
                    should_break = True
                
                if should_update:
                    break

            if should_update:
                break

digit_chars = "1234567890"

lines = open("inp5.txt", "r").readlines()

seeds = list(map(int, lines[0].removeprefix("seeds: ").split()))
intervals = []
for i in range(len(seeds)//2):
    intervals.append((seeds[i*2], seeds[i*2] + seeds[i*2+1]))
update_intervals(intervals)

maps = []
current_map = []

for i in range(len(lines)):
    line = lines[i]
    if line[0] in digit_chars:
        current_map.append(list(map(int, line.split())))
    if len(current_map) != 0 and (line[0] not in digit_chars or i == len(lines)-1):
        maps.append(current_map)
        current_map = []

for i in range(len(maps)):

    dest_intervals = []

    current_map = maps[i]
    for j in range(len(current_map)):

        dest_begin = current_map[j][0]
        source_begin = current_map[j][1]
        length = current_map[j][2]

        k = 0
        while k < len(intervals):

            interval = intervals[k]

            lo = interval[0]
            hi = interval[1]

            if (lo >= source_begin and lo <= source_begin + length) or (hi >= source_begin and hi <= source_begin + length) or (lo <= source_begin and hi >= source_begin + length):
                
                intervals.remove(interval)

                intersection = (max(lo, source_begin), min(hi, source_begin + length))
                intersection_dest = (intersection[0] - source_begin + dest_begin, intersection[1] - source_begin + dest_begin)
                dest_intervals.append(intersection_dest)

                if lo < source_begin:
                    intervals.append((lo, source_begin - 1))
                if hi > source_begin + length:
                    intervals.append((source_begin + length + 1, hi))

            else:
                k += 1

    for dest_interval in dest_intervals:
        intervals.append(dest_interval)


lowest_lo = 10**100
for interval in intervals:
    if interval[0] < lowest_lo:
        lowest_lo = interval[0]

print(lowest_lo)
