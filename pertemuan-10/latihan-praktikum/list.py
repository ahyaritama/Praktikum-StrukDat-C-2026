stack = []

# Push
stack.append("https://www.google.com")
stack.append("https://classroom.google.com")
stack.append("https://www.w3schools.com")
stack.append("https://drive.google.com")
stack.append("https://classroom.google.com")
print("Stack: ", stack)

# Peek
topElement = stack[-1]
print("Peek:", topElement)

# Pop
poppedElement = stack.pop()
print("Pop:", poppedElement)

# Stack after Pop
print("Stack after Pop:", stack)

# isEmpty
isEmpty = not bool(stack)
print("isEmpty:", isEmpty)

# Size
print("Size:",len(stack))

# Back
stack.pop()
print("History:", stack)