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

def compute_first(symbol):
    if symbol in first_table:
        return first_table[symbol].copy()

    first=set()
    if(symbol.islower()):   
        first.add(symbol)
    else:
        for lhs_rule in grammar[symbol]:    
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
