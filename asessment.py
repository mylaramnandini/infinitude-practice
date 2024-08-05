import sys
my = {'python': 50, 'social': 75, 'science': 70}
print(type(my))
print(my.pop('python'))
print('the size is', sys.getsizeof(my), 'bytes')
statement = "the escape character is \"escape\" it allows the double quotes in it"
print(statement)
age = 22
txt = f"the age is {age}"
print(txt)
name = "Alice"
age = 30
my_string = f"Name: {name}, Age: {age}"
print(my_string)
# the above line is f-string formatting
name = "Alice"
age = 30
my_string2 = "Name: {}, Age: {}".format(name, age)
print(my_string2)
# the above concatenation is done using format method
my_tuple = ("Python", "is", "awesome")
my_string3 = " ".join(my_tuple)
print(my_string3)
# the above one is used to concatenate string with list or tuple using jion method
print(id(my_string))

# assesment-2 4-7-24

my_dict = {'python': 50, 'science': 70, 'social': 89, 'math': 94, 'c': 88}
for i in my_dict:
    print(i)
for i in my_dict:
    print(my_dict[i])
# in the above program we are printing keys and values separately without using values and keys function
# question 1 a
# print(my_dict.pop('c')) requires a specific key  to remove key-value and optionally provides a default value.
# if the given key is not present in dict. my_dict.pop(key[, default])
# print(my_dict)
my_dict.popitem()
print(my_dict)
# while popitem() is useful when you need to remove the last inserted item.

# question 1.b add the following key & pair i;e "car":"Tesla" to the dictionary if the key exists then
# it should update the value otherwise it should add the Key
if "car" in my_dict:  # to check key present in dictionary use "in"
    my_dict["car"] = "tesla"
else:
    my_dict.setdefault("car", 'tesla')
print(my_dict)

# question1.c covert dictionary into list
mylist = list(my_dict.items())
print(mylist)

# question2 b
list1 = [10, 20, 10, 30, 90, 'nandini', 'krishna', 60, 50, 50]
print(list1[:8])
print(list1[8])

# question2 c
list1=sorted(list1, key=str)
print(list1)
list1.reverse()
print(list1)

# question2 d
x = input()
reversed_string = ''
for char in x:
    reversed_string = char + reversed_string
print(reversed_string)

# question 3
for i in range(1, 101):
    if i % 5 == 0:
        print(i)
print('end of the loop')









