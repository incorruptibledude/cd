grammar={
    'E':['F*E','F'],
    'F':['T+F','T'],
    'T':['i','(E)']
}

leading_table={}
def compute_leading(symbol):
    # print(leading_table)
    if symbol in leading_table:
        return leading_table[symbol]
    temp=set()
    for rule in grammar[symbol]:
        if(len(rule)==1):
            if(not rule.isupper()):
                temp.add(rule)
            else:
                temp.update(compute_leading(rule))
        elif(len(rule)==3):
            if(not rule[0].isupper()):
                temp.add(rule[0])
            else:
                temp.add(rule[1])
                if(not rule[0]==symbol):    #left recursion
                    temp.update(compute_leading(rule[0])) 
    leading_table[symbol]=temp.copy()
    return leading_table[symbol]


compute_leading('E')
for nonterm in leading_table:
    print(f'LEADING({nonterm})={leading_table[nonterm]}')
            
