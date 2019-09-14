
input = open("binarize.in", "r")
outfile = open("binarize.out", 'w')
input.readline()
for line in input:
    count = 0
    bin = 0
    while (bin < int(line)):
        bin = 2 ** count
        count += 1
    outfile.write("Input value: " + line)
    outfile.write(str(bin) + "\n\n")
