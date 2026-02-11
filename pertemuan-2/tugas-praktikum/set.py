# OUTPUT TIDAK AKAN SELALU SAMA, KARENA SET MENAMPILKAN ISINYA SECARA ACAK!

# Python Set
myset = {"apple", "banana", "cherry"}
print(myset) # Output: {'apple', 'banana', 'cherry'}

# Access Set
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
# Output:
# banana
# apple
# cherry

# Add Item to Set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset) # Output: {'apple', 'cherry', 'orange', 'banana'}

# Add Item from Another Iterable
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) # {'mango', 'apple', 'pineapple', 'banana', 'papaya', 'cherry'}

# Remove Item from Set
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) # Output: {'apple', 'cherry'}

thisset.discard("apple")
print(thisset) # Output: {'cherry'}

# Remove Random Item from Set
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) # Output: apple
print(thisset) # Output: {'banana', 'cherry'}

# Join Set with Iterable
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) # Output: {'b', 1, 'a', 2, 3, 'c'}

# Update Set
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1) # Output: {1, 2, 3, 'a', 'b', 'c'}

# Set Intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3) # Output: {'apple'}

# Set Difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3) # Output: {'banana', 'cherry'}

# Set Symmetric Difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3) # Output: {'microsoft', 'banana', 'google', 'cherry'}

# Frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x) # Output: frozenset({'apple', 'cherry', 'banana'})
print(type(x)) # Output: <class 'frozenset'>