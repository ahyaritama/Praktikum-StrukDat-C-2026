class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name) # Output: Emil
print(p1.age) # Output: 36

p1.age = 26
print(p1.age) # Output: 26

del p1.age
# print(p1.age)
# AttributeError: 'Person' object has no attribute 'age'