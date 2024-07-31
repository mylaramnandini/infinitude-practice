a ={1, 2, 3, 4, 5, 1, 3, 1}
print(a.remove(3))
# remove function is used to remove a specific element from set without index as set is unodered
print(a)
a.add(3)
print(a)
# add function is used to add a element
b = a.pop()
# Use the pop function to remove and return an arbitrary element or any element
print('popped element:', b)
print(a)
b = a.copy()
# use the copy function
print(b)
b.clear()
# use clear fuction to clear the whole set
print(b)
b = {1, 4, 6, 8}
# c = a.union(b) 1method
c = a | b # 2nd method for union
print(c)
difference = a.difference(b) # difference = a-b another method
print(difference)
# Difference: Contains elements from a that are not in b

# symmetric_difference = a ^ b another method
print(a.symmetric_difference(b))
# gives output results in elements that are in a and b but not in both
print(a.isdisjoint(b))
# If the sets are disjoint (i.e., their intersection is empty), the method returns True; otherwise, it returns False
print(a.issubset(c))
# here a is subset of c so it returns true in output i.e all elements of a are present in c set
d = [10, 20, 30]
a.update(d)
print(a)
# update Adds multiple elements to the set from another iterable (like a set, list, tuple, or dictionary).
