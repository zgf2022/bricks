print ("infile ")
infilename = str(input())
print ("infile 2")
infilename2 = str(input())
print ("outfilename")
outfilename = str(input())



lines_seen = set() # holds lines already seen
outfile = open(outfilename, "w")
for line in open(infilename, "r"):
	if line not in lines_seen: # not a duplicate
		Linecontents = line.split()
		print (str(Linecontents))
		x = int(Linecontents[1])
		y = int(Linecontents[3])
		z = int(Linecontents[5]) 
		if (x > 0) and (y > 0) and (z > 0):
			lineout = str(x) + ", " + str(y) + ", " + str(z) + "\n"
			outfile.write(lineout)
		lines_seen.add(line)
for line in open(infilename2, "r"):
	if line not in lines_seen: # not a duplicate
		Linecontents = line.split()
		print (str(Linecontents))
		x = int(Linecontents[1])
		y = int(Linecontents[3])
		z = int(Linecontents[5]) 
		if (x > 0) and (y > 0) and (z > 0):
			lineout = str(x) + ", " + str(y) + ", " + str(z) + "\n"
			outfile.write(lineout)
		lines_seen.add(line)
outfile.close()