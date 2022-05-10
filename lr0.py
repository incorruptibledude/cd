gram = {
	"S":["CC"],
	"C":["aC","d"]
}
start = "S"
terms = ["a","d","$"]

non_terms = []
for i in gram:
	non_terms.append(i)
gram["S'"]= [start]


new_row = {}
for i in terms+non_terms:
	new_row[i]=""


non_terms += ["S'"]
# each row in state table will be dictionary {nonterms ,term,$}
stateTable = []
# I = [(terminal, closure)]
# I = [("S","A.A")]

def Closure(term, I):
	if term in non_terms:
		for i in gram[term]:
			I+=[(term,"."+i)]
	I = list(set(I))
	for i in I:
		# print("." != i[1][-1],i[1][i[1].index(".")+1])
		if "." != i[1][-1] and i[1][i[1].index(".")+1] in non_terms and i[1][i[1].index(".")+1] != term:
			I += Closure(i[1][i[1].index(".")+1], [])
	return I

Is = []
Is+=set(Closure("S'", []))


countI = 0
omegaList = [set(Is)]
while countI<len(omegaList):
	newrow = dict(new_row)
	vars_in_I = []
	Is = omegaList[countI]
	countI+=1
	for i in Is:
		if i[1][-1]!=".":
			indx = i[1].index(".")
			vars_in_I+=[i[1][indx+1]]
	vars_in_I = list(set(vars_in_I))
	# print(vars_in_I)
	for i in vars_in_I:
		In = []
		for j in Is:
			if "."+i in j[1]:
				rep = j[1].replace("."+i,i+".")
				In+=[(j[0],rep)]
		if (In[0][1][-1]!="."):
			temp = set(Closure(i,In))
			if temp not in omegaList:
				omegaList.append(temp)
			if i in non_terms:
				newrow[i] = str(omegaList.index(temp))
			else:
				newrow[i] = "s"+str(omegaList.index(temp))
			print(f'Goto(I{countI-1},{i}):{temp} -- I{omegaList.index(temp)}')
		else:
			temp = set(In)
			if temp not in omegaList:
				omegaList.append(temp)
			if i in non_terms:
				newrow[i] = str(omegaList.index(temp))
			else:
				newrow[i] = "s"+str(omegaList.index(temp))
			print(f'Goto(I{countI-1},{i}):{temp} -- I{omegaList.index(temp)}')

	stateTable.append(newrow)
print("\n\nList of states\n")
for i in omegaList:
	print(f'I{omegaList.index(i)}: {i}')
