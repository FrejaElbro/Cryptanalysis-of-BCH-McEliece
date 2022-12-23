from math import log,floor

# Function to test if L is well-formed
def WellFormed(L,p,s,m):
	sigma = 1+ floor(log(max(L),p))
	wellformed = sigma < s*m
	for a in range(sigma):
		wellformed = wellformed and (p**a in L)
	included = 1
	for b in range(2,p):
		bincluded = True
		for a in range(sigma):
			bincluded = bincluded and (b*p**a in L);
		if bincluded and included != b-1:
			wellformed = False
		elif bincluded and included == b-1:
			included = b
	return wellformed


# Run through following output file and report results
file1 = open('Lresultsq27.csv', 'r')

# Setup variables to use
haswellformed = True
p = 1
s = 1
m = 1
r = 1
q = 1

# Read lines one by one
while True:
	line = file1.readline()
	if not line:
		break
	linelist = line.strip().split(";")

	# The following condition checks if we are reading the header-line. In that case, do nothing
	if len(linelist[6]) > 8: 
		continue
	
	# The following will activate if we are reading a line with parameters
	# Here we report on the previous parameters, and initialise new parameters
	elif len(linelist[1]) > 0: 
		if not haswellformed:
			print("First failed r", r)
			# If you want to see the first Ls that fail, uncomment the following
			#for i in range(len(Ls)):
			#	print(Ls[i])
		p = int(linelist[0])
		s = int(linelist[1])
		mnew = int(linelist[2])
		r = int(linelist[3])
		q = p**s
		haswellformed = False
		if m != mnew:
			m = mnew
			print("q",q,"m",m)
		Ls = []
	
	# The following will activate if we a reading a line which contains an L
	elif len(linelist[0]) > 1:
		stringlist = linelist[0].replace("]","").replace("[","").replace(" ","").split(",")
		intlist = []
		for intstring in stringlist:
			if intstring != "":
				intlist.append(int(intstring))
		Ls.append(intlist)
		WF = WellFormed(intlist,p,s,m)
		if WF == True:
			haswellformed = True

file1.close()


# Report on the last results
if haswellformed == False:
	print("First failed r", r)
	# If you want to see the first Ls that fail, uncomment the following
	#for i in range(len(Ls)):
	#	print(Ls[i])
else:
	print("still working r",r)


  

  

