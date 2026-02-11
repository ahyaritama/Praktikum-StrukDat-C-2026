# Python Tuple
mytuple = ("apple", "banana", "cherry")
mysingletuple = ("apple",)
print(mytuple) # Output: ('apple', 'banana', 'cherry')
print(mysingletuple) # Output: ('apple',)

# Access Tuple using Index
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) # Output: banana

# Access Tuple using Negative Index
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) # Output: cherry

# Access Tuple using Range Index
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) # Output: ('cherry', 'orange', 'kiwi')

# Update Tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) # Output: ('apple', 'kiwi', 'cherry')

# Add Item to Tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple) # Output: ('apple', 'banana', 'cherry', 'orange')

# Remove Item from Tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple) # Output: ('banana', 'cherry')

# Unpack Tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green) # Output: apple
print(yellow) # Output: banana
print(red) # Output: cherry

# Unpack Tuple with Asterisk (*)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green) # Output: apple
print(yellow) # Output: banana
print(red) # Output: ['cherry', 'strawberry', 'raspberry']

# Loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
# Output:
# apple
# banana
# cherry

# Join Tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3) # Output: ('a', 'b', 'c', 1, 2, 3)

# Multiply Tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple) # Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

