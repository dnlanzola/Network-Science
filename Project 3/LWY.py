# (r modulo 5) x 20 ; (r modulo 5) x 20 + 30
# (3 modulo 5) x 20 ; (3 modulo 5) x 20 + 30
#      3 x 20		;       60 + 30 
#	     60			; 		   90


from networkx import nx

def activate_nodes(fileN, p, beginRange, endRange, outFileName):
	# READ GRAPH FROM FILE
	g = nx.read_edgelist(fileN)
	#g = nx.read_weighted_edgelist(fileN)

	# SORT BY DEGREE
	sorted(g.degree, key=lambda x: x[1], reverse=True)

	# SET ATTRIBUTE 0 TO ALL NODES 
	attr = 0
	nx.set_node_attributes(g, attr, 'attr')
	
	att = nx.get_node_attributes(g, 'attr')
	#print att
	
	numNodes = 0
	
	for k, v in att.items():
		numNodes = numNodes + 1
		#print("Key : {0}, Value : {1}".format(k, v))
		
	#numNodes = number_of_nodes(g)
	
	
	if (p == 0.3):
		# RANGE ADJUST
		a = 100 - beginRange
		b = 100 - endRange
	
		beginAtt = (a * numNodes) / 100
		endAtt = (b * numNodes) / 100

		# FINAL POSITIONS OF RANGE ON DICTIONARY
		beginAtt = numNodes - beginAtt
		endAtt = numNodes - endAtt
	
		while (beginAtt <= endAtt):
			att[att.keys()[beginAtt]] = 1
			beginAtt = beginAtt + 1
		
		#for k, v in att.items():
			#print("Key : {0}, Value : {1}".format(k, v))

	if (p == 0.2):
		# RANGE ADJUST
		a = 100 - beginRange
		b = 100 - (endRange - 10)
	
		beginAtt = (a * numNodes) / 100
		endAtt = (b * numNodes) / 100

		# FINAL POSITIONS OF RANGE ON DICTIONARY
		beginAtt = numNodes - beginAtt
		endAtt = numNodes - endAtt
	
		while (beginAtt <= endAtt):
			att[att.keys()[beginAtt]] = 1
			beginAtt = beginAtt + 1
		
		#for k, v in att.items():
			#print("Key : {0}, Value : {1}".format(k, v))


	if (p == 0.1):
		# RANGE ADJUST
		a = 100 - beginRange
		b = 100 - (endRange - 20)
	
		beginAtt = (a * numNodes) / 100
		endAtt = (b * numNodes) / 100

		# FINAL POSITIONS OF RANGE ON DICTIONARY
		beginAtt = numNodes - beginAtt
		endAtt = numNodes - endAtt
	
		while (beginAtt <= endAtt):
			att[att.keys()[beginAtt]] = 1
			beginAtt = beginAtt + 1
		
		#for k, v in att.items():
			#print("Key : {0}, Value : {1}".format(k, v))



	if (p == 0.05):
		# RANGE ADJUST
		a = 100 - beginRange
		b = 100 - (endRange - 25)
	
		beginAtt = (a * numNodes) / 100
		endAtt = (b * numNodes) / 100

		# FINAL POSITIONS OF RANGE ON DICTIONARY
		beginAtt = numNodes - beginAtt
		endAtt = numNodes - endAtt
	
		while (beginAtt <= endAtt):
			att[att.keys()[beginAtt]] = 1
			beginAtt = beginAtt + 1
		
		#for k, v in att.items():
			#print("Key : {0}, Value : {1}".format(k, v))

	
	nx.set_node_attributes(g, att, 'attr')
	nx.write_edgelist(g, outFileName+".elist.txt", data=['attr'])
	
	
	#att = nx.get_node_attributes(g, 'attr')
	#for k, v in att.items():
	#	print("Key : {0}, Value : {1}".format(k, v))	
	
	measure_MI(g)




def measure_MI(g):
	
	att = nx.get_node_attributes(g, 'attr')
	fraction = 0
	
	for k, v in att.items():
		if (v == 0):
			activeNeighbors = [nbr for nbr in g.neighbors(k) if g.node[nbr]['attr']>0.5]
			tNeighbors = [n for n in g.neighbors(k)]
			
			totalNeighbors = len(tNeighbors)
			totalActive = len(activeNeighbors)
			
			if ( totalActive >= (totalNeighbors / 2) ):
				fraction = fraction + 1
			
	print "Total Number of Neighbors: ", totalNeighbors
	
	print "Fraction: ", fraction
	r = nx.degree_assortativity_coefficient(g)
	print "Attribute Assortativity Coeff: "
	print(nx.attribute_assortativity_coefficient(g,'attr'))
	
	r = nx.degree_pearson_correlation_coefficient(g)
	print "Degree Pearson Correlation Coefficient: "
	print("%3.1f"%r)



#MAIN

p = 0.05
fileName = "imdb_actor"

fileNameT = fileName + ".elist.txtFFdiv10.txt"

array = [0.05, 0.1, 0.2, 0.3]

i = 0

while (i < 4):
	outFile = fileNameT + "-p:" + str(array[i])
	print outFile
	activate_nodes(fileNameT, array[i], 60, 90, outFile)
	i = i + 1








