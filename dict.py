first = {'python': 50, 'science': 70, 'social': 89, 'math': 94, 'c': 88}
print(first.items())
# returns a list containing tuple of key value pairs
print(first.values())
print(first.keys())
b = {'nandini': 9.8, 'social': 10}
first.update(b)
print(first)
c = [('d', 6), ('e', 8)]
first.update(c)
print(first)
# we use update to add another dictionary or multiple key-value pairs to a dictionary
# You can also use update with an iterable of key-value pairs:
# here iterable is list, set, tuple consisting od key-value pairs like above list
first.setdefault('salesforce', 98)
print(first)
# The setdefault method is used to insert a key with a specified value if the key is not already present.
# If the key is present, it returns the current value associated with the key.
print(first.copy())
first['d'] = 9
first['f'] = 4
print(first)
# by above method we can update the value of an existing key by giving key and can also add a new key.



