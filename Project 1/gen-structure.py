import snap

# --- PART 1 ---
print "-- SIZE OF NETWORK --"
print ""

# (a) Number of Nodes (b) Number of Edges
G1 = snap.LoadEdgeList(snap.PNGraph, "p2p-Gnutella04.txt", 0, 1)
print "Number of nodes in Gnutella p2p Network: %d" % (G1.GetNodes())
print "Number of edges in Gnutella p2p Network: %d" % (G1.GetEdges())
print ""

G1c = snap.LoadEdgeList(snap.PNGraph, "p2p-Gnutella04.txt", 1, 0)

G2 = snap.LoadEdgeList(snap.PNGraph, "as-caida20040105.txt", 0, 1)
print "Number of nodes in AS from CAIDA: %d" % (G2.GetNodes())
print "Number of edges in AS from CAIDA: %d" % (G2.GetEdges())
print ""

G2c = snap.LoadEdgeList(snap.PNGraph, "as-caida20040105.txt", 1, 0)

G3 = snap.LoadEdgeList(snap.PNGraph, "Wiki-Vote.txt", 0, 1)
print "Number of nodes in Wiki-Vote: %d" % (G3.GetNodes())
print "Number of edges in Wiki-Vote: %d" % (G3.GetEdges())
print ""

G3c = snap.LoadEdgeList(snap.PNGraph, "Wiki-Vote.txt", 1, 0)

# Generating Random Graph with 5000 nodes
G4 = snap.GenRndGnm(snap.PNGraph, 5000, 50000)
print "Number of nodes in  random5000by6: %d" % (G4.GetNodes())
print "Number of edges in  random5000by6: %d" % (G4.GetEdges())
snap.SaveEdgeList(G4, "random5000by6.txt", "Save as tab-separated list of edges")
print ""

G4c = snap.LoadEdgeList(snap.PNGraph, "random5000by6.txt", 1, 0)

# --- PART 2 ---

# (a) Number of nodes with degree = 1
print "-- DEGREE OF NODES IN THE NETWORK --"
print ""
print "Number of nodes with degree = 1 in Gnutella p2p Network: %d" %  snap.CntDegNodes(G1, 1)

print "Number of nodes with degree = 1 in AS from CAIDA: %d" %  snap.CntDegNodes(G2, 1)

print "Number of nodes with degree = 1 in Wiki-Vote.txt: %d" %  snap.CntDegNodes(G3, 1)

print "Number of nodes with degree = 1 in random5000by6: %d" %  snap.CntDegNodes(G4, 1)



print ""
# (b) Node id(s) for the node(s) with the highest degree
print "Node id(s) with highest degree in Gnutella p2p Network: "
highestDegree = 0
for NI in G1.Nodes():
    if (NI.GetOutDeg() + NI.GetInDeg()) > highestDegree:
        highestDegree = NI.GetOutDeg() + NI.GetInDeg()


for NI in G1.Nodes():
    if (NI.GetOutDeg() + NI.GetInDeg()) == highestDegree:
        print "%d, " % NI.GetId()

print "Node id(s) with highest degree in AS from CAIDA: "
highestDegree = 0
for NI in G2.Nodes():
    if (NI.GetOutDeg() + NI.GetInDeg()) > highestDegree:
        highestDegree = NI.GetOutDeg() + NI.GetInDeg()

for NI in G2.Nodes():
    if (NI.GetOutDeg() + NI.GetInDeg()) == highestDegree:
        print "%d, " % NI.GetId()

print "Node id(s) with highest degree in Wiki-Vote.txt: "
highestDegree = 0
for NI in G3.Nodes():
    if (NI.GetOutDeg() + NI.GetInDeg()) > highestDegree:
        highestDegree = NI.GetOutDeg() + NI.GetInDeg()

for NI in G3.Nodes():
    if (NI.GetOutDeg() + NI.GetInDeg()) == highestDegree:
        print "%d, " % NI.GetId()

print "Node id(s) with highest degree in random5000by6: "
highestDegree = 0
for NI in G4.Nodes():
    if (NI.GetOutDeg() + NI.GetInDeg()) > highestDegree:
        highestDegree = NI.GetOutDeg() + NI.GetInDeg()

for NI in G4.Nodes():
    if (NI.GetOutDeg() + NI.GetInDeg()) == highestDegree:
        print "%d, " % NI.GetId()

print ""
# (c) For nodes with degree = 1. Show average degree of the node's 2-hop neighborhood

nodesDegreeOne = []
averageD = 0;
count = 1;
if snap.CntDegNodes(G1, 1) == 0:
	print "There are no nodes with degree 1 in Gnutella p2p Network."
else:	
	for NI in G1.Nodes():
    		if (NI.GetOutDeg() + NI.GetInDeg()) == 1:
        		nodesDegreeOne.append(NI.GetId())

		NodeVec = snap.TIntPrV()

	for NI in nodesDegreeOne:
		NodeVec = snap.TIntV()
		snap.GetNodesAtHop(G1, NI, 2, NodeVec, True)
		for item in NodeVec:
			averageD = averageD + item
			count = count + 1
		print "The average degree of %d 's 2-hop neighborhood is: %d" % (NI, averageD/count)


nodesDegreeOne = []
averageD = 0;
count = 1;
if snap.CntDegNodes(G2, 1) == 0:
	print "There are no nodes with degree 1 in AS from CAIDA."
else:	
	for NI in G1.Nodes():
    		if (NI.GetOutDeg() + NI.GetInDeg()) == 1:
        		nodesDegreeOne.append(NI.GetId())

		NodeVec = snap.TIntPrV()

	for NI in nodesDegreeOne:
		NodeVec = snap.TIntV()
		snap.GetNodesAtHop(G1, NI, 2, NodeVec, True)
		for item in NodeVec:
			averageD = averageD + item
			count = count + 1
		print "The average degree of %d 's 2-hop neighborhood is: %d" % (NI, averageD/count)


nodesDegreeOne = []
averageD = 0;
count = 1;
if snap.CntDegNodes(G3, 1) == 0:
	print "There are no nodes with degree 1 in Wiki-Vote.txt."
else:	
	for NI in G1.Nodes():
    		if (NI.GetOutDeg() + NI.GetInDeg()) == 1:
        		nodesDegreeOne.append(NI.GetId())

		NodeVec = snap.TIntPrV()

	for NI in nodesDegreeOne:
		NodeVec = snap.TIntV()
		snap.GetNodesAtHop(G1, NI, 2, NodeVec, True)
		for item in NodeVec:
			averageD = averageD + item
			count = count + 1
		print "The average degree of %d 's 2-hop neighborhood is: %d" % (NI, averageD/count)


nodesDegreeOne = []
averageD = 0;
count = 1;
if snap.CntDegNodes(G4, 1) == 0:
	print "There are no nodes with degree 1 in random5000by6."
else:	
	for NI in G1.Nodes():
    		if (NI.GetOutDeg() + NI.GetInDeg()) == 1:
        		nodesDegreeOne.append(NI.GetId())

		NodeVec = snap.TIntPrV()

	for NI in nodesDegreeOne:
		NodeVec = snap.TIntV()
		snap.GetNodesAtHop(G1, NI, 2, NodeVec, True)
		for item in NodeVec:
			averageD = averageD + item
			count = count + 1
		print "The average degree of %d 's 2-hop neighborhood is: %d" % (NI, averageD/count)






print ""
# (d) Plot of the degree distribution

snap.PlotInDegDistr(G1, "DD_gnutellap2pnetwork", "Directed graph - in-degree Distribution")
print "Degree distribution of Gnutella p2p Network is in: DD_gnutella.png"

snap.PlotInDegDistr(G2, "DD_asfromcaida", "Directed graph - in-degree Distribution")
print "Degree distribution of AS from CAIDA is in: DD_asfromcaida.png"

snap.PlotInDegDistr(G3, "DD_wikivote", "Directed graph - in-degree Distribution")
print "Degree distribution of Wiki-Vote is in: DD_wikivote.png"

snap.PlotInDegDistr(G4, "DD_random5000by6", "Directed graph - in-degree Distribution")
print "Degree distribution of random5000by6 is in: DD_random5000by6.png"


print ""
# --- PART 3 ---
print "-- PATHS IN THE NETWORK --"
# (a) Approximate Full Diameter (maximum shortest path)

mean = 0
result = snap.GetBfsFullDiam(G1, 10, False)
rlist = []
rlist.append(result)
print "Approx. diameter in Gnutella p2p Network with sampling number 10 nodes: %d" % result
result = snap.GetBfsFullDiam(G1, 100, False)
rlist.append(result)
print "Approx. diameter in Gnutella p2p Network with sampling number 100 nodes: %d" % result
result = snap.GetBfsFullDiam(G1, 1000, False)
rlist.append(result)
print "Approx. diameter in Gnutella p2p Network with sampling number 1000 nodes: %d" % result
mean = sum(rlist) / 3
variance = sum((xi - mean) ** 2 for xi in rlist) / 3
print "Approx. diameter in Gnutella p2p Network (mean and variance): %d, %d" % (mean, variance)


print ""
mean = 0
result = snap.GetBfsFullDiam(G2, 10, False)
rlist = []
rlist.append(result)
print "Approx. diameter in AS from CAIDA with sampling number 10 nodes: %d" % result
result = snap.GetBfsFullDiam(G2, 100, False)
rlist.append(result)
print "Approx. diameter in AS from CAIDA with sampling number 100 nodes: %d" % result
result = snap.GetBfsFullDiam(G2, 1000, False)
rlist.append(result)
print "Approx. diameter in AS from CAIDA with sampling number 1000 nodes: %d" % result
mean = sum(rlist) / 3
variance = sum((xi - mean) ** 2 for xi in rlist) / 3
print "Approx. diameter in AS from CAIDA (mean and variance): %d, %d" % (mean, variance)


print ""
mean = 0
result = snap.GetBfsFullDiam(G3, 10, False)
rlist = []
rlist.append(result)
print "Approx. diameter in Wiki-Vote with sampling number 10 nodes: %d" % result
result = snap.GetBfsFullDiam(G3, 100, False)
rlist.append(result)
print "Approx. diameter in Wiki-Vote with sampling number 100 nodes: %d" % result
result = snap.GetBfsFullDiam(G3, 1000, False)
rlist.append(result)
print "Approx. diameter in Wiki-Vote with sampling number 1000 nodes: %d" % result
mean = sum(rlist) / 3
variance = sum((xi - mean) ** 2 for xi in rlist) / 3
print "Approx. diameter in Wiki-Vote (mean and variance): %d, %d" % (mean, variance)


print ""
mean = 0
result = snap.GetBfsFullDiam(G4, 10, False)
rlist = []
rlist.append(result)
print "Approx. diameter in random5000by6 with sampling number 10 nodes: %d" % result
result = snap.GetBfsFullDiam(G4, 100, False)
rlist.append(result)
print "Approx. diameter in random5000by6 with sampling number 100 nodes: %d" % result
result = snap.GetBfsFullDiam(G4, 1000, False)
rlist.append(result)
print "Approx. diameter in random5000by6 with sampling number 1000 nodes: %d" % result
mean = sum(rlist) / 3
variance = sum((xi - mean) ** 2 for xi in rlist) / 3
print "Approx. diameter in random5000by6 (mean and variance): %d, %d" % (mean, variance)




print ""
# (b) Effective Diameter & Variance

result = snap.GetBfsEffDiam(G1, 10, False)
rlist = []
rlist.append(result)
print "Approx. effective diameter in Gnutella p2p Network with sampling number 10 nodes: %d" % result
result = snap.GetBfsEffDiam(G1, 100, False)
rlist.append(result)
print "Approx. effective diameter in Gnutella p2p Network with sampling number 100 nodes: %d" % result
result = snap.GetBfsEffDiam(G1, 1000, False)
rlist.append(result)
print "Approx. effective diameter in Gnutella p2p Network with sampling number 1000 nodes: %d" % result


mean = sum(rlist) / 3
variance = sum((xi - mean) ** 2 for xi in rlist) / 3
print "Approx. diameter in Gnutella p2p Network (mean and variance): %d, %d" % (mean, variance)


print ""
result = snap.GetBfsEffDiam(G2, 10, False)
rlist = []
rlist.append(result)
print "Approx. effective diameter in AS from CAIDA with sampling number 10 nodes: %d" % result
result = snap.GetBfsEffDiam(G2, 100, False)
rlist.append(result)
print "Approx. effective diameter in AS from CAIDA with sampling number 100 nodes: %d" % result
result = snap.GetBfsEffDiam(G2, 1000, False)
rlist.append(result)
print "Approx. effective diameter in AS from CAIDA with sampling number 1000 nodes: %d" % result


mean = sum(rlist) / 3
variance = sum((xi - mean) ** 2 for xi in rlist) / 3
print "Approx. diameter in AS from CAIDA (mean and variance): %d, %d" % (mean, variance)


print ""
result = snap.GetBfsEffDiam(G4, 10, False)
rlist = []
rlist.append(result)
print "Approx. effective diameter in Wiki-Vote with sampling number 10 nodes: %d" % result
result = snap.GetBfsEffDiam(G4, 100, False)
rlist.append(result)
print "Approx. effective diameter in Wiki-Vote with sampling number 100 nodes: %d" % result
result = snap.GetBfsEffDiam(G4, 1000, False)
rlist.append(result)
print "Approx. effective diameter in Wiki-Vote with sampling number 1000 nodes: %d" % result


mean = sum(rlist) / 3
variance = sum((xi - mean) ** 2 for xi in rlist) / 3
print "Approx. diameter in Wiki-Vote (mean and variance): %d, %d" % (mean, variance)



print ""
result = snap.GetBfsEffDiam(G3, 10, False)
rlist = []
rlist.append(result)
print "Approx. effective diameter in random5000by6 with sampling number 10 nodes: %d" % result
result = snap.GetBfsEffDiam(G3, 100, False)
rlist.append(result)
print "Approx. effective diameter in random5000by6 with sampling number 100 nodes: %d" % result
result = snap.GetBfsEffDiam(G3, 1000, False)
rlist.append(result)
print "Approx. effective diameter in random5000by6 with sampling number 1000 nodes: %d" % result


mean = sum(rlist) / 3
variance = sum((xi - mean) ** 2 for xi in rlist) / 3
print "Approx. diameter in random5000by6 (mean and variance): %d, %d" % (mean, variance)


print ""
# (c) Plot Distribution of the Shortest Path Lengths

snap.PlotShortPathDistr(G1, "SP_gnutellap2p", "Directed graph - shortest path")
print "Shortest path distribution of Genutella p2p Network is in: SP_gnutellap2p.png"

snap.PlotShortPathDistr(G2, "SP_asfromcaida", "Directed graph - shortest path")
print "Shortest path distribution of AS from CAIDA is in: SP_asfromcaida.png"

snap.PlotShortPathDistr(G3, "SP_wikivote", "Directed graph - shortest path")
print "Shortest path distribution of Wiki-Vote is in: SP_wikivote.png"

snap.PlotShortPathDistr(G4, "SP_random5000by6", "Directed graph - shortest path")
print "Shortest path distribution of random5000by6 is in: SP_random5000by6.png"




print ""
# --- PART 4 ---

# (a) Fraction of nodes in the largest connected component
print "Fraction of nodes in largest connected component in Gnutella p2p network: %d " % snap.GetMxSccSz(G1)
print "Fraction of nodes in largest connected component in AS from CAIDA: %d " % snap.GetMxSccSz(G2)
print "Fraction of nodes in largest connected component in Wiki-Vote: %d " % snap.GetMxSccSz(G3)
print "Fraction of nodes in largest connected component in random5000by6: %d " % snap.GetMxSccSz(G4)

print ""
# (b) Fraction of nodes in the largest connected component of the complement of the real graph

print "Fraction of nodes in largest connected component in Gnutella p2p network's complement: %d " % snap.GetMxSccSz(G1c)
print "Fraction of nodes in largest connected component in AS from CAIDA's complement: %d " % snap.GetMxSccSz(G2c)
print "Fraction of nodes in largest connected component in Gnutella Wiki-Vote's complement: %d " % snap.GetMxSccSz(G3c)
print "Fraction of nodes in largest connected component in Gnutella p2p network's complement: %d " % snap.GetMxSccSz(G4c)

print ""
# (c) Plot of the distribution of sizes of connected components

snap.PlotSccDistr(G1, "SD_gnutellap2p", "Directed graph - scc distribution")
print "Component size distribution of Gnutella p2p network is in: SD_gnutellap2p"

snap.PlotSccDistr(G2, "SD_asfromcaida", "Directed graph - scc distribution")
print "Component size distribution of AS from CAIDA is in: SD_asfromcaida"

snap.PlotSccDistr(G3, "SD_wikivote", "Directed graph - scc distribution")
print "Component size distribution of Wiki-Vote is in: SD_wikivote"

snap.PlotSccDistr(G4, "SD_random5000by6", "Directed graph - scc distribution")
print "Component size distribution of random5000by6k is in: SD_random5000by6"


print ""
snap.PlotSccDistr(G1c, "SD_gnutellap2pC", "Directed graph - scc distribution")
print "Component size distribution of Gnutella p2p network's complement is in: SD_gnutellap2pC"

snap.PlotSccDistr(G2c, "SD_asfromcaidaC", "Directed graph - scc distribution")
print "Component size distribution of AS from CAIDA's complement is in: SD_asfromcaidaC"

snap.PlotSccDistr(G3c, "SD_wikivoteC", "Directed graph - scc distribution")
print "Component size distribution of Wiki-Vote's complement is in: SD_wikivoteC"

snap.PlotSccDistr(G4c, "SD_random5000by6C", "Directed graph - scc distribution")
print "Component size distribution of random5000by6k's complement is in: SD_random5000by6C"





