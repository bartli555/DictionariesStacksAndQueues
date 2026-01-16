import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
   # Using a list as a stack
   stack = []
   # Dictionary for matching pairs
   pairs = {')': '(', ']': '[', '}': '{'}

   for char in expression:
      if char in "({[":
         stack.append(char)
      elif char in ")}]":
         if not stack:
            return False
         
         top = stack.pop()
         if pairs[char] != top:
            return False
            
   # If stack is empty, all brackets were matched
   return len(stack) == 0

if brackets_ok(expression1):
   print("Expression 1: Brackets OK")
else:
   print("Expression 1: Brackets NOT Correct")

if brackets_ok(expression2):
   print("Expression 2: Brackets OK")
else:
   print("Expression 2: Brackets NOT Correct")

if brackets_ok(expression3):
   print("Expression 3: Brackets OK")
else:
   print("Expression 3: Brackets NOT Correct")