file  = open("input.txt").read().strip().split("\n")


completion = []

for x in file:
    x = x[x.find(": ") + 2:]
    x = x.split(";")
    y = [z.split(", ") for z in x]

    completable = True

    redmax   = 12
    greenmax = 13
    bluemax  = 14

    for zz in y:
        for xx in zz:
            number, name = xx.strip().split(" ")
            if int(number) > redmax and name == "red":
                completable = False
            if int(number) > bluemax and name == "blue":
                completable = False
            if int(number) > greenmax and name == "green":
                completable = False
    completion.append(completable)

print(completion)
competionsum = 0

for yy in range(0, len(completion)):
    if completion[yy] == True:
        competionsum += yy + 1

print(competionsum)
