# Python List
mylist = ["apple", "banana", "cherry"]
print(mylist) # Output: ['apple', 'banana', 'cherry']

# Access List using Index
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # Output: banana

# Access List using Negative Index
thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) # Output: cherry

# Access List using Range Index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # Output: ['cherry', 'orange', 'kiwi']

# Access List using Negative Range Index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) # Output: ['orange', 'kiwi', 'melon']

# Check if Items Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list") # Output: Yes, 'apple' is in the fruits list

# Change Item Value using Index
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) # Output: ['apple', 'blackcurrant', 'cherry']

# Change Item Values using Range Index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) # Output: ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

# Insert New Item
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) # Output: ['apple', 'banana', 'watermelon', 'cherry']

# Append Item
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # Output: ['apple', 'banana', 'cherry', 'orange']

# Insert Item
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) # Output: ['apple', 'orange', 'banana', 'cherry']

# Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) # Output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# Remove Specified Item from List
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # Output: ['apple', 'cherry']

# Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # Output: ['apple', 'cherry']

# Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # Output: []

# Loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
# Output: 
# apple
# banana
# cherry

# Sort Ascending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) # Output: ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) # Output: ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

# Copy List
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) # Output: ["apple", "banana", "cherry"]

# Join List
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) # Output: ['a', 'b', 'c', 1, 2, 3]