file  = open("input.txt").read().strip().split("\n")


completion = []
completionpower = []

for x in file:
    x = x[x.find(": ") + 2:]
    x = x.split(";")
    y = [z.split(", ") for z in x]

    redlimit   = 0
    greenlimit = 0
    bluelimit  = 0

    for zz in y:
        for xx in zz:
            number, name = xx.strip().split(" ")

            if name == "red" and int(number) > redlimit:
                redlimit = int(number)

            if name == "blue" and int(number) > bluelimit:
                bluelimit = int(number)

            if name == "green" and int(number) > greenlimit:
                greenlimit = int(number)

    completionpower.append([redlimit, greenlimit, bluelimit])

total = 0
for x in completionpower:
    total += x[0] * x[1] * x[2]

print(total)
print(completionpower)
