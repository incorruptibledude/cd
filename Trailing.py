grammar={
    'E':['F*E','F'],
    'F':['T+F','T'],
    'T':['i','(E)']
}
trailing_table={}
def compute_trailing(symbol):
    # print(leading_table)
    if symbol in trailing_table:
        return trailing_table[symbol]
    temp=set()
    for rule in grammar[symbol]:
        if(len(rule)==1):
            if(not rule.isupper()):
                temp.add(rule)
            else:
                temp.update(compute_trailing(rule))
        elif(len(rule)==3):
            if(not rule[2].isupper()):
                temp.add(rule[2])
            else:
                temp.add(rule[1])
                if(not rule[2]==symbol):    #right recursion
                    temp.update(compute_trailing(rule[2])) 
    trailing_table[symbol]=temp.copy()
    return trailing_table[symbol]

compute_trailing('E')
for nonterm in trailing_table:
    print(f'TRAILING({nonterm})={trailing_table[nonterm]}')