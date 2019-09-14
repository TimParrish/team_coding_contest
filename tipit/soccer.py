input = open("soccer.in", "r")
outfile = open("soccer.out", 'w')

teams = [][]

T = int(input.readline())

for i in range(T):
    line = input.readline()
    found1 = False
    found2 = False
    data[] = line.split()

    for j in range(len(teams[])):
        if(teams[j][0] == data[0]):
            teams[j][1] += data[1]
            found1 = True
            break
        if(teams[j][0] == data[3]):
            teams[j][1] += data[3]
            found2 = True
            break
    if(not found1):
        teams[len(teams[])][0] = data[0]
        teams[len(teams[])][1] = data[1]
    if(not found2):
        teams[len(teams[])][0] = data[0]
        teams[len(teams[])][1] = data[1]
