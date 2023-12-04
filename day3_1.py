
grid = open("inp3.txt", "r").readlines()

digit_chars = "1234567890"

h = len(grid)
w = len(grid[0])-1

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

            # check if a symbol other than '.' exists around the range [num_lo, num_hi]

            in_num = False

            has_sym = False

            if num_lo > 0:
                if grid[i][num_lo-1] != ".":
                    has_sym = True
                if i > 0:
                    if grid[i-1][num_lo-1] != ".":
                        has_sym = True
                if i < h-1:
                    if grid[i+1][num_lo-1] != ".":
                        has_sym = True
            
            if num_hi < w-1:
                if grid[i][num_hi+1] != ".":
                    has_sym = True
                if i > 0:
                    if grid[i-1][num_hi+1] != ".":
                        has_sym = True
                if i < h-1:
                    if grid[i+1][num_hi+1] != ".":
                        has_sym = True
            
            if i > 0:
                for j2 in range(num_lo, num_hi+1):
                    if grid[i-1][j2] != ".":
                        has_sym = True
            
            if i < h-1:
                for j2 in range(num_lo, num_hi+1):
                    if grid[i+1][j2] != ".":
                        has_sym = True
        
            if has_sym:
                s += int(grid[i][num_lo : num_hi+1])

print(s)
