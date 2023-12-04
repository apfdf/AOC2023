
grid = open("inp3.txt", "r").readlines()

digit_chars = "1234567890"

h = len(grid)
w = len(grid[0])-1

nums = []
syms = []

s = 0

for i in range(h):
    
    num_lo = 0
    num_hi = 0

    in_num = False
    
    for j in range(w):
        
        if grid[i][j] in digit_chars:
            if in_num:
                num_hi = j
            else:
                in_num = True
                num_lo = j
                num_hi = j
        if in_num and (grid[i][j] not in digit_chars or grid[i][j] in digit_chars and j == w-1):
            in_num = False
            nums.append((num_lo, num_hi, i, int(grid[i][num_lo : num_hi+1])))
        if grid[i][j] not in digit_chars and grid[i][j] != ".":
            syms.append((i, j))


for sym in syms:

    sym_i = sym[0]
    sym_j = sym[1]

    adjacent = []
    
    for num in nums:

        num_lo = num[0]
        num_hi = num[1]
        num_i = num[2]
        val = num[3]

        is_adjacent = False

        if num_i == sym_i:
            if num_hi == sym_j-1:
                is_adjacent = True
            if num_lo == sym_j+1:
                is_adjacent = True
        if (num_i == sym_i+1 or num_i == sym_i-1) and num_lo <= sym_j+1 and num_hi >= sym_j-1:
            is_adjacent = True
        
        if is_adjacent:
            adjacent.append(val)

    if len(adjacent) == 2:
        s += adjacent[0] * adjacent[1]

print(s)
