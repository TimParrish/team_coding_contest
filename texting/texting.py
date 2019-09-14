input = open("texting.in", "r")
outfile = open("texting.out", 'w')

legend_count = int(input.readline())
print(legend_count)

translate = {}


for i in range(legend_count):
    line = input.readline()
    currentLine = line.split(" ", 1)
    translate[currentLine[0]] = currentLine[1].strip()


cypher_count = int(input.readline())

for i in range(cypher_count):
    line = input.readline().split()
    print(line, str(i))
    for j in line:
        found = False
        for k, v in translate.items():
            if (j == k):
                outfile.write(v + " ")
                found = True
        if (not found):
            outfile.write(j + " ")
    outfile.write("\n")
