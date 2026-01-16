# Reverse string using a stack
def reverse_string(text):
    stack = []
    # Push all characters to stack
    for char in text:
        stack.append(char)
    
    reversed_text = ""
    # Pop characters (LIFO order)
    while len(stack) > 0:
        reversed_text += stack.pop()
        
    return reversed_text

text = "Hello World"
print(f"Original: {text}")
print(f"Reversed: {reverse_string(text)}")