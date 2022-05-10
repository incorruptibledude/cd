def generate3ac(pos):
    stk=[]
    operators=['*','+','-','/']
    t=1
    for ch in pos:
        if ch not in operators:
            stk.append(ch)
        else:
            print(f't{t}:={stk[-2]}{ch}{stk[-1]}')
            stk.pop(); stk.pop()
            stk.append(f't{t}')
            t+=1

def quadruple(pos):
    stk=[]
    operators=['*','+','-','/']
    t=1
    for ch in pos:
        if ch not in operators:
            stk.append(ch)
        else:
            print(stk[-2].center(5) , ch.center(5) , stk[-1].center(5) , f't{t}'.center(5))
            stk.pop(); stk.pop()
            stk.append(f't{t}')
            t+=1

def triple(pos):
    stk=[]
    operators=['*','+','-','/']
    t=0
    for ch in pos:
        if ch not in operators:
            stk.append(ch)
        else:
            print(stk[-2].center(5) , ch.center(5) , stk[-1].center(5))
            stk.pop(); stk.pop()
            stk.append(f'({t})')
            t+=1

pos='abc*+d-'
# pos='a=b+c-d'
print('3 address code')
generate3ac(pos)
print('\nQuadruple')
quadruple(pos)
print('\nTriple')
triple(pos)

