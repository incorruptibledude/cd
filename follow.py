# S -> ACB | Cbb | Ba
# A -> da | BC
# B -> g | Є
# C -> h | Є

grammar = {
    'S':['ACB','Cbb','Ba'],
    'A':['da','BC'],
    'B':['g','e'],
    'C':['h','e']
}

first_table=dict()


#################
#COMPUTATION OF FIRST
#################
def compute_first(symbol):
    if symbol in first_table:
        return first_table[symbol].copy()

    first=set()
    if(symbol.islower()):   #terminal
        first.add(symbol)
    else:
        for lhs_rule in grammar[symbol]:    #iterate through each rule
            i=0
            while(i<len(lhs_rule)):
                temp=compute_first(lhs_rule[i]).copy()
                if 'e' in temp:
                    if(i!=(len(lhs_rule)-1)):
                        temp.remove('e')
                    first.update(temp)
                else:
                    first.update(temp)
                    break
                i+=1

    first_table[symbol]=first
    return first     

compute_first('S')
for symbol in first_table:
    print(f'First({symbol}) =',first_table[symbol])


##################
#COMPUTATION OF FOLLOW
##################
follow_table=dict()
def follow(nT):
    #print("inside follow({})".format(nT))
    follow_ = set()
    #print("FOLLOW", FOLLOW)
    prods = grammar.items()
    if nT=='S':
        follow_ = follow_ | {'$'}
    for nt,rhs in prods:
        #print("nt to rhs", nt,rhs)
        for alt in rhs:
            for char in alt:
                if char==nT:
                    following_str = alt[alt.index(char) + 1:]
                    if following_str=='':
                        if nt==nT:
                            continue
                        else:
                            follow_ = follow_ | follow(nt)
                    else:
                        follow_2 = set()
                        for s in following_str:
                            follow_2.update(first_table[s])
                        if 'e' in follow_2:
                            follow_ = follow_ | follow_2-{'e'}
                            follow_ = follow_ | follow(nt)
                        else:
                            follow_ = follow_ | follow_2
    #print("returning for follow({})".format(nT),follow_)
    follow_table[nT]=follow_.copy()
    return follow_


for rhs in grammar:
    follow(rhs)
    for lhs_rule in grammar[rhs]:
        for s in lhs_rule:
            if s.isupper():
                follow(s)

for k in follow_table:
    print(f'Follow({k}) = ',follow_table[k])
