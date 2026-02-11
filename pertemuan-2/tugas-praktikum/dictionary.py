# Python Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Access Dictionary using Key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x) # Output: Mustang

x = thisdict.get("year")
print(x) # Output: 1964

# Access All Keys
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x) # Output: dict_keys(['brand', 'model', 'year'])

# Access All Values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x) # Output: dict_values(['Ford', 'Mustang', 1964])

# Access All Keys and Values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x) # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# Check if Key Exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
# Output: Yes, 'model' is one of the keys in the thisdict dictionary

# Change Value
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

# Add Item (Key & Value)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# Update Value
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# Remove Item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict) # Output: {'brand': 'Ford', 'year': 1964}

# Remove Last Item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang'}

# Loop
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
# Output:
# brand Ford
# model Mustang
# year 1964

# Copy Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}