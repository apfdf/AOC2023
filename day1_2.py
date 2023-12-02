
lines = open("inp1.txt", "r").readlines()

digit_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digit_chars = "123456789"

s = 0

for line in lines:

    digit1 = 0
    digit2 = 0

    for i in range(len(line)):

        if line[i] in digit_chars:
            digit1 = int(line[i])
            break

        should_break = False
        for digit_string in digit_strings:
            if len(digit_string) <= len(line) - i - 1:
                if line[i : i + len(digit_string)] == digit_string:
                    digit1 = digit_strings.index(digit_string) + 1
                    should_break = True
                    break
        
        if should_break:
            break
    
    for i in range(len(line)):

        if line[len(line) - 1 - i] in digit_chars:
            digit2 = int(line[len(line) - 1 - i])
            break
        
        should_break = False
        for digit_string in digit_strings:
            if len(digit_string) <= i:
                if line[len(line) - i - 1 : len(line) - i - 1 + len(digit_string)] == digit_string:
                    digit2 = digit_strings.index(digit_string) + 1
                    should_break = True
                    break
                    
        if should_break:
            break

    print(str(digit1) + " " + str(digit2))
    
    s += 10 * digit1 + digit2

print(s)
