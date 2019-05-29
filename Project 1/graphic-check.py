from networkx import nx



with open('ds1.txt') as f:
    array = []
    for line in f: # read rest of lines
        num = int(line)
        array.append(num)


if nx.is_graphical(array,method='eg') == True:
    print "ds1.txt is a graphic degree sequence."
else:
    print "ds1.txt is NOT a graphic degree sequence. It fails the Erdos-Gallai algorithm."

with open('ds2.txt') as f:
    array = []
    for line in f: # read rest of lines
        num = int(line)
        array.append(num)


if nx.is_graphical(array,method='eg') == True:
    print "ds2.txt is a graphic degree sequence."
else:
    print "ds2.txt is NOT a graphic degree sequence. It fails the Erdos-Gallai algorithm."

with open('ds3.txt') as f:
    array = []
    for line in f: # read rest of lines
        num = int(line)
        array.append(num)


if nx.is_graphical(array,method='eg') == True:
    print "ds3.txt is a graphic degree sequence."
else:
    print "ds3.txt is NOT a graphic degree sequence. It fails the Erdos-Gallai algorithm."

with open('ds4.txt') as f:
    array = []
    for line in f: # read rest of lines
        num = int(line)
        array.append(num)


if nx.is_graphical(array,method='eg') == True:
    print "ds4.txt is a graphic degree sequence."
else:
    print "ds4.txt is NOT a graphic degree sequence. It fails the Erdos-Gallai algorithm."

