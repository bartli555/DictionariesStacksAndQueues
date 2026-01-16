import queue

# Stack implementation using a list for simplicity
stack = []

n = 18
temp_n = n

# Convert to binary
while temp_n > 0:
    remainder = temp_n % 2
    stack.append(remainder)
    temp_n = temp_n // 2

print(f"Natural number: {n}")
print("Binary number: ", end="")

# Print result by popping from stack
while len(stack) > 0:
    print(stack.pop(), end="")

print() # New line