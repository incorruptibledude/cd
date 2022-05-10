grammar={'E':[['E','+','E'],['E','*','E'],['id']]}

#operator precedence function table
function_table={
    'f':{'id':4,'+':2,'*':4,'$':0},
    'g':{'id':5,'+':1,'*':3,'$':0}
}

#string to parse
input='id + id * id'

input=input.split(' ')
print(''.join(input),end='\n\n')
input.append('$')
stk=['$']


p=0
parsed_string=[]

print('Stack'.ljust(10,' '),'Input'.ljust(10,' '),'Action'.ljust(15,' '),'Parsed string')
print(''.join(stk).ljust(10,' '),''.join(input[p:]).ljust(10,' '),''.join(parsed_string).ljust(10,' '))



#Stack Implementation of Operator Precedence shift-reduce Parsing 
try:
    while(not(stk[-1]=='$' and input[p]=='$')):
        a=function_table['f'][stk[-1]]
        b=function_table['g'][input[p]]
        # print(stk[-1],input[p],a,b)

        shifted=False
        #SHIFT
        if(a<=b):
            stk.append(input[p])    #PUSH to stack
            parsed_string.append(input[p])  
            p+=1
            shifted=True

        #REDUCE
        elif(a>b):
            to_reduce=stk.pop(-1)   #POP from stack
            #search appropriate rule to reduce
            for lhs in grammar:
                for rhs in grammar[lhs]:
                    if to_reduce in rhs:
                        reduce_rule=[lhs,rhs]
            
            #find index of operator which is to be reduced from the back
            ind=len(parsed_string) - 1 - parsed_string[::-1].index(to_reduce)

            l=len(reduce_rule[1])
            m=l//2
            parsed_string=parsed_string[:ind-m]+[reduce_rule[0]]+parsed_string[ind+(l-m):]

            #reduction rule is of type : E->id
            # if(len(reduce_rule[1])==1):
                # parsed_string=parsed_string[:ind]+[reduce_rule[0]]+parsed_string[ind+1:]
            
            #reduction rule is of type : E->E+E
            # elif(len(reduce_rule[1])==3):
                # parsed_string=parsed_string[:ind-1]+[reduce_rule[0]]+parsed_string[ind+2:]

        action='SHIFT' if shifted else 'REDUCE '+str(reduce_rule[0])+'->'+''.join(reduce_rule[1])
        #print table row
        print(''.join(stk).ljust(10,' '),''.join(input[p:]).ljust(10,' '),
        action.ljust(15,' '),
        ''.join(parsed_string).ljust(10,' '))
    
    print('Accepted')

except(Exception):
    print('Not accepted')
