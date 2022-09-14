print("\n"*100) # Unnecessary Line: to clear up the console for a better presentation. Yes.

stack = [] 

# Adding Elements to the stack (using append() function to push)
stack.append('a')
stack.append('b')
stack.append('c')

## Display Current Stack
print(f"Initial Stack: {stack} \n")

# Removing Elements from the stack (using pop() function to remove)
print("Removing Elements: ")
for i in range(2): # Removing 2 Elements
    print(f"> {stack.pop()}")

## Display Final Stack
print(f"\nFinal Stack: {stack}")