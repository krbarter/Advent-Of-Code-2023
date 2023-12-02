import re

file  = open("input.txt", "r")
lines = file.readlines()

output  = 0
output2 = 0

for x in range(0, len(lines)):
    y = lines[x].split("\n")[0]
    print(y)

    # Part One
    linelist = []
    for z in range(0, len(y)):
        if y[z].isdigit():
            linelist.append(y[z])

    if len(linelist) > 1:
        output += (int(linelist[0] + linelist[-1]))

    #Part Two
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    p = "(?=(" + "|".join(numbers) + "|\\d))"
    digits = re.findall(p, y)

    def f(x):
        if x in numbers:
            return str(numbers.index(x) + 1)
        else:
            return x
        
    digits = [*map(f, digits)]
    output2 += (int (digits[0] + digits[-1]))


print(output)
print(output2)