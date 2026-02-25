class Person:
    pass

class MyClass:
    x = 5

p1 = MyClass()
print(p1.x) # Output: 5

del p1
# print(p1) | NameError: name 'p1' is not defined

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x) # Output: 5
print(p2.x) # Output: 5