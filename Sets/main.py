# names = {"Ravi","Santhosh","Naveen","Balaji","Ravi"}
# print(names)

# The add() method adds an element to the set.
# If the element already exists, the add() method does not add the element.
# names = {"Ravi","Santhosh","Naveen","Balaji"}
# names.add("Kiran")
# print(names)


# The clear() method removes all elements in a set
# names = {"Ravi","Santhosh","Naveen","Balaji"}
# names.clear()
# print(names)


# The copy() method copies the set.
# names = {"Ravi","Santhosh","Naveen","Balaji"}
# x = names.copy()
# print(x)



# The difference() method returns a set that contains the difference between two sets.
# Meaning: The returned set contains items that exist only in the first set,
#          and not in both sets.
# names1 = {"Ravi","Santhosh","Naveen","Balaji"}
# names2 = {"RBR","Sai","Ravi"}
# x = names1.difference(names2)
# print(x)



#The difference_update() method removes the items that exist in both sets.
# names1 = {"Ravi","Santhosh","Naveen","Balaji"}
# names2 = {"RBR","Sai","Ravi"}
# names1.difference_update(names2)
# print(names1)




# The discard() method removes the specified item from the set.
# names1 = {"Ravi","Santhosh","Naveen","Balaji"}
# names1.discard("Ravi")
# print(names1)



# The intersection() method returns a set that contains
#   the similarity between two or more sets.
# names1 = {"Ravi","Santhosh","Naveen","Balaji"}
# names2 = {"RBR","Sai","Ravi"}
# x = names1.intersection(names2)
# print(x)



# The intersection_update() method removes the items that is not present in both sets
# (or in all sets if the comparison is done between more than two sets).
# names1 = {"Ravi","Santhosh","Naveen","Balaji"}
# names2 = {"RBR","Sai","Ravi"}
# names1.intersection_update(names2)
# print(names1)


# The isdisjoint() method returns True if none of the items are present in both sets,
# otherwise it returns False.
# names1 = {"Ravi","Santhosh","Naveen","Balaji"}
# names2 = {"RBR","Sai","Ravi"}
# z = names1.isdisjoint(names2)
# print(z)



# The issubset() method returns True if all items in the set exists in the specified set,
# otherwise it returns False.
# x = {"a","b","c"}
# y = {"a","b","c","d","e","f"}
# z = x.issubset(y)
# print(z)



# The issuperset() method returns True if all items in the specified set exists
# # in the original set, otherwise it returns False.
# x = {"a","b","c","d","e","f"}
# y = {"a","b","c"}
# z = x.issuperset(y)
# print(z)




# The pop() method removes a random item from the set.
# This method returns the removed item.
# names = {"Ravi","Santhosh","Naveen","Balaji"}
# names.pop()
# print(names)



# The remove() method removes the specified element from the set.
# names = {"Ravi","Santhosh","Naveen","Balaji"}
# names.remove("Naveen")
# print(names)



# The union() method returns a set that contains all items from the original set,
#     and all items from the specified set(s).
# You can specify as many sets you want, separated by commas.
# It does not have to be a set, it can be any iterable object.
# If an item is present in more than one set, the result will contain
#      only one appearance of this item.
# names1 = {"Ravi","Santhosh","Naveen","Balaji"}
# names2 = {"RBR","Sai","Ravi"}
# z = names1.union(names2)
# print(z)




# The update() method updates the current set,
# by adding items from another set (or any other iterable).
names1 = {"Ravi","Santhosh","Naveen","Balaji"}
names2 = {"RBR","Sai","Ravi"}
names1.update(names2)
print(names1)