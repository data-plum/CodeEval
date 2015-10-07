import sys

def prefix_expressions(my_file):
	with open(my_file, 'r') as f:	
		for string in f:
			token_list = string.split()
			operand_stack = []
			operator_stack = []
			result = 0
			for token in token_list:
				if token in "+*/":
					operator_stack.append(token)
				else:
					if not operand_stack:
						operand_stack.append(token)	
					else:
						op2 = float(token)
						op1 = float(operand_stack.pop())
						op = operator_stack.pop()
						if op == "*":
							result = op1 * op2
						elif op == "/":
							result = op1 / op2
						elif op == "+":
							result = op1 + op2
						operand_stack.append(result)
			print int(operand_stack.pop())


prefix_expressions(sys.argv[1])