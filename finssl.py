OPERATORS = set(['+', '-', '*', '/', '(', ')','$','^'])
PRI = {'+':1, '-':1, '*':2, '/':2, '$':3, '^':3}

### INFIX ===> POSTFIX ###
def infix_to_postfix(formula):
    stack = [] # only pop when the coming op has priority 
    output = ''
    count = 0
    for ch in formula:
        count+=1
        print(f'---------------------------Step  {count}----------------------------')
        print(f'operand : {ch}\t\t')
        if ch not in OPERATORS:
            output += ch
            #print(f'Postfix : {output}')
        elif ch == '(':
            stack.append('(')
            #print(f'stack : {stack}')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
                #print(f'Postfix : {output}')
            stack.pop() # pop '('
            #print(f'stack : {stack}')
        else:
            while stack and stack[-1] != '(' and PRI[ch] <= PRI[stack[-1]]:
                output += stack.pop()
                #print(f'Postfix : {output}')
            stack.append(ch)
            #print(f'stack : {stack}')
        print(f'stack : {stack}\t\t')
        print(f'Postfix : {output}')
    # leftover
    while stack: 
    	output += stack.pop()
    print('---------------------------------------------------------------------')
    print(f'POSTFIX: {output}')
    print('---------------------------------------------------------------------')
    return output

### INFIX ===> PREFIX ###
def infix_to_prefix(formula):
    convert=''
    for ch in formula:
        if ch == '(':
            convert += ')'
        elif ch == ')':
            convert +='('
        else :
            convert += ch

    rev1 = convert[::-1]	
    print('------------------------Reverse String-------------------------------')
    print(f'Reversed String : {rev1}')	

    stack = [] # only pop when the coming op has priority 
    output = ''
    count = 0
    for ch in rev1:
        count+=1
        print(f'---------------------------Step  {count}----------------------------')
        print(f'operand : {ch}\t\t')
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop() # pop '('
        else:
            while stack and stack[-1] != '(' and PRI[ch] <= PRI[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
        print(f'stack : {stack}\t\t')
        print(f'Prefix : {output}')
    # leftover
    while stack: 
    	output += stack.pop()
    print('---------------------------Reverse Prefix--------------------------------')
    rev2 = output[::-1]
    print(f'PREFIX: {rev2}')
    print('---------------------------------------------------------------------')
    return rev2
    
### THREE ADDRESS CODE GENERATION ###
def generate3AC(pos):
	print("### THREE ADDRESS CODE GENERATION ###")
	exp_stack = []
	t = 1
	
	for i in pos:
		if i not in OPERATORS:
			exp_stack.append(i)
		else:
			print(f't{t} := {exp_stack[-2]} {i} {exp_stack[-1]}')
			exp_stack=exp_stack[:-2]
			exp_stack.append(f't{t}')
			t+=1
	print('---------------------------------------------------------------------')

expres = input("INPUT THE EXPRESSION: ")
pre = infix_to_prefix(expres)
pos = infix_to_postfix(expres)
generate3AC(pos)






