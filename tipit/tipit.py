input = open("tipit.in", "r")
outfile = open("tipit.out", 'w')


def roundCheck(num):
    float(num) + 0.00
    snum = str(num)
    snum = snum[-2:]
    snum = float(snum)
    if (snum == 0.00):
        return 0
    else:
        return 1


def main():
    input.readline()

    for line in input:
        notDone = True
        meal_cost = int(line)
        tip = round((meal_cost*.2), 2)

        tip += roundCheck(tip)

        tip = int(tip)

        ntip = tip + meal_cost
        while notDone:
            if (str(ntip)[::-1]) == str(ntip):
                outfile.write("Input cost: " + str(meal_cost) + "\n")
                outfile.write(str(ntip-meal_cost) + " " + str(ntip) + "\n\n")
                notDone = False
            ntip = int(ntip)
            ntip += 1


main()
