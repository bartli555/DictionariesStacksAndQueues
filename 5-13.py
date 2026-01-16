expression = "2 3 + 5 *" # (2+3)*5 = 25
tokens = expression.split()
stack = []

for token in tokens:
    if token.isdigit():
        stack.append(int(token))
    else:
        val2 = stack.pop()
        val1 = stack.pop()
        if token == "+":
            stack.append(val1 + val2)
        elif token == "*":
            stack.append(val1 * val2)

print(f"Result: {stack[0]}")