# E-> E+T|E-T|T
# A -> Aa|b  ===  A->bA', A'->aA'|e

class Compiler:
    def __init__(self,grammar):
        self.grammar=grammar
        print('Original grammar')
        self.print_grammar()       

    def print_grammar(self,grammar=None):
        if(not grammar):
            grammar=self.grammar
        for key in grammar:
            print(key+' -> ',end='')
            for lhs_rule in grammar[key]:
                print(lhs_rule+'|',end='')
            print()
        print()

    #check if a production is left-recursive
    def prod_is_recursive(self,start_terminal,grammar=None):
        if(not grammar):
            grammar=self.grammar
        for lhs_prod in grammar[start_terminal]:
            if lhs_prod[0]==start_terminal:
                return True
        return False

    #removes recursion from a left-recursive production rule
    def remove_recursion(self,start_terminal,grammar=None):
        if(not grammar):
            grammar=self.grammar
        temp=[]     #store right-recursive rules
        temp2=[]    
        for lhs_prod in grammar[start_terminal]:
            if lhs_prod[0]==start_terminal:
                temp.append(lhs_prod[1:])
            else:
                temp2.append(lhs_prod+start_terminal+"'")

        temp=[ r+start_terminal+"'" for r in temp]
        temp.append('e')

        new_prods=dict()
        new_prods[start_terminal]=temp2
        new_prods[start_terminal+"'"]=temp

        return new_prods

    #check if each production is left-recursive, if yes then remove it
    def recursion_free(self,grammar=None):
        if(not grammar):
            grammar=self.grammar
        new_grammar=dict()
        for start_terminal in grammar:
            if(self.prod_is_recursive(start_terminal)):
                new_grammar.update(self.remove_recursion(start_terminal))
            else:
                new_grammar[start_terminal]=grammar[start_terminal]

        print('Before removing left-recursion')
        self.print_grammar()
        print('After removing left-recursion')
        self.print_grammar(new_grammar)


grammar={'E':['E+T','E-T','T']}
gr1=Compiler(grammar)
gr1.recursion_free()


