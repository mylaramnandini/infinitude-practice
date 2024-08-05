# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
#
# largest = max(num1, num2, num3)
# print("Largest number:", largest)


# num = int(input("Enter a number: "))
# sum_result = sum(range(1, num + 1))
# print("Sum:", sum_result)

# def is_palindrome(s):
#   return s == s[::-1]
#
# string = input("Enter a string: ")
# if is_palindrome(string):
#   print("Palindrome")
# else:
#   print("Not a palindrome")
#

# """def fact(n):
#     if n == 0:
#         return 1
#     return n* fact(n-1)
# n = int(input("give the number:"))
# print(fact(n)


# def count_vowels(s):
#   vowels = "aeiouAEIOU"
#   return sum(1 for char in s if char in vowels)
#
# string = input("Enter a string: ")
# print("Number of vowels:", count_vowels(string))


# string = "hello world"
# new_string = string.replace('l', 'L')
# print(new_string)

# lst = [10, 25, 7, 30, 15]
# max_element = max(lst)
# print("Maximum element:", max_element)

# def are_anagrams(str1, str2):
#   return sorted(str1) == sorted(str2)
#
# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")
# if are_anagrams(string1, string2):
#   print("Anagrams")
# else:
#   print("Not anagrams")

# sentence = input("Enter a sentence: ")
# words = sentence.split()
# max_length = max(len(word) for word in words)
# print("Length of the longest word:", max_length)


""""n = int(input())
my =dict()
for i in range(n+1):
    my[i]=i*i
print(my)"""

# import math
# c=50
# h=30
# value = []
# # items=[x for x in input().split(',')]
# items = input().split(",")
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
#
# print(','.join(value))


# items= input().split(',')
# items.sort()
# print(','.join(items))


# class InputOutString(object):
#     def __init__(self):
#         self.s = ""
#
#     def getString(self):
#         self.s = input()
#
#     def printString(self):
#         print(self.s.upper())
#
# strObj = InputOutString()
# strObj.getString()
# strObj.printString()


# items = input().split(" ")
# x =sorted(list(set(items)))
# y = " ".join(x)
# print(y)

# lines =[]
# while True:
#     s = input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break
# for line in lines:
#     print(line)


# x = input().split(",")
# list =[]
# for i in x:
#     if int(i, 2)%5 ==0: # binary conversion
#         list.append(i)
#     else:
#         pass
# print (",".join(list))


# list =[]
# for i in range(1000, 3001):
#     if i%2==0:
#         x =str(i)
#         for j in x:
#              if int(j)%2 != 0:
#                  # all_even = False
#                  break
#         if int(j)%2 == 0:
#             # all_even = True
#             list.append(x)
#
# print(",".join(list))
# method 2
# values = []
# for i in range(1000, 3001):
#     s = str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         values.append(s)
# print (",".join(values))


# s = input("enter the input:")
# Letters = 0
# Digits =0
# for c in s:
#     if c.isalpha():
#         Letters+=1
#     elif c.isdigit():
#         Digits+=1
#     else:
#         pass
# print("LETTERS:",Letters)
# print("DIGITS:", Digits)


# s = input()
# d={"DIGITS":0, "LETTERS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass
# print "LETTERS", d["LETTERS"]
# print "DIGITS", d["DIGITS"]


# s = input()
# upper = 0
# lower = 0
# for c in s:
#     if c.isupper():
#         upper+=1
#     elif c.islower():
#         lower+=1
#     else:
#         pass
#
# print("upper letters :",upper)
# print("lower letters are:",lower)


# a = input()
# term1 = int(a)
# term2= int(a * 2)
# term3 = int(a * 3)
# term4 = int(a * 4)
#
# def summation(a):
#     print(term1+term2+term3+term4)
#
# summation(a)


# a = input()
# list = (a.split(","))
# numbers =[int(x) ** 2 for x in list if int(x)%2!=0]
# print(numbers)
# once again refer the question 16

# def compute(transactions):
#     net_amount = 0
#     for transaction in transactions:
#         parts = transaction.split()
#         if len(parts) < 2:
#             print(f"Ignoring invalid transaction: {transaction}")
#             continue
#
#         if parts[0] == 'D':
#             try:
#                 amount = int(parts[1])
#                 net_amount += amount
#             except ValueError:
#                 print(f"Invalid amount for deposit: {parts[1]}")
#         elif parts[0] == 'W':
#             try:
#                 amount = int(parts[1])
#                 net_amount -= amount
#             except ValueError:
#                 print(f"Invalid amount for withdrawal: {parts[1]}")
#
#     return net_amount


# if __name__ == "__main__":
#     print("Enter transactions (format: D amount or W amount), one per line:")
#
#     transactions = []
#     while True:
#         transaction = input().strip()
#         if not transaction:
#             break
#         transactions.append(transaction)
#
#     net_amount = compute(transactions)
#     print(f"Net amount in the bank account: {net_amount}

# netAmount = 0
# while True:
#     s = input()
#     if not s:
#         break
#     values = s.split(" ")
#     operation = values[0]
#     amount = int(values[1])
#     if operation=="D":
#         netAmount+=amount
#     elif operation=="W":
#         netAmount-=amount
#     else:
#         pass
# print (netAmount)
# revise it

# import re
# s = input("enter the passwords:").split(",")
# list = []
# pattern =r'[#@$]'
# for i in s:
#     if(i.__len__()>5 and i.__len__()<13 ):
#         if re.search("[a-z]",i ) and re.search("[A-Z]",i) and re.search("[0-9]",i) and re.search(pattern,i):
#             list.append(i)
#         else:
#             pass
#     else:
#         pass
# if list:
#     print("Valid passwords:", ",".join(list))
# else:
#     print("No valid passwords found.")

# l = []
# while True:
#     s = input()
#     if not s:
#         break
#     l.append(tuple(s.split(",")))
# print(sorted(l, key = lambda x:[x[0],x[1],x[2]]))


# import math
# s= input()
# p =[0,0] # here y i.e down and up direction is p[1], here x i.e right and left direction is p[0]
# l= s.split(",")
# for x in l:
#     x = x.split(" ")
#     if x[0] == "UP":
#         p[1]+=int(x[1])
#     elif x[0] == "DOWN":
#         p[1]-=int(x[1])
#     elif x[0] == "RIGHT":
#         p[0]+=int(x[1])
#     elif x[0] == "LEFT":
#         p[0]-=int(x[1])
#     else:
#         pass
# print(round(math.sqrt(p[0]**2+p[1]**2)))


# another solution
# import math
# pos = [0,0]
# while True:
#     s = input()
#     if not s:
#         break
#     movement = s.split(" ")
#     direction = movement[0]
#     steps = int(movement[1])
#     if direction=="UP":
#         pos[0]+=steps
#     elif direction=="DOWN":
#         pos[0]-=steps
#     elif direction=="LEFT":
#         pos[1]-=steps
#     elif direction=="RIGHT":
#         pos[1]+=steps
#     else:
#         pass
#
# print int(round(math.sqrt(pos[1]**2+pos[0]**2)))


# freq = {}
# s = input("enter the input:")
# for word in s.split():
#       freq[word] =freq.get(word, 0)+1
#
# l = list(freq.keys())
# l.sort()
# count={}
# for w in l:
#       count[w]=freq.get(w,0)
# print(count)

# another book solution
# freq = {}   # frequency of words in text
# line = input()
# for word in line.split():
#     freq[word] = freq.get(word,0)+1
#
# words = freq.keys()
# words.sort()
#
# for w in words:
#     print ("%s:%d" % (w,freq[w]))

# def add(a, b):
#     """this function is used to add two strings
#      the inputs are two number""" # here we definitely need to provide triple quotes
#     print(a+b)
#
# print(add.__doc__)

# def int(n):
#     return str(n)
#
# def sum(s1, s2):
#     s =int(s1) + int(s2)
#     print(s)
#
# def con(s1, s2):
#     return s1+s2
#
# print(con("bx","bas"))

# def length(s1,s2):
#     if s1.__len__() > s2.__len__():
#         print(s1 + ":", s1.__len__())
#     elif s2.__len__()>s1.__len__():
#         print(s2 + ":",s2.__len__())
#     else:
#         print(s1 ,"\n", s2)
#
# length("nandini","kanha")
#

# def num(n):
#     if n%2 ==0:
#         print("the number is even")
#     else:
#         print("the number is odd")


# def dictionary(n):
#     freq={}
#     for i in range(1,n+1):
#         freq[i]=i**2
#     print(freq)
#     for k,v in freq.items():
#         print(k)
#         print(v)
#     print(freq.values())
#     print(freq.keys())
# dictionary(3)


#26
# def list():
#     l =[]
#     for i in range(1,21):
#         l.append(i**2)
#     print(l)
# list()


#27
# def list():
#     l =[]
#     for i in range(1,21):
#         l.append(i**2)
#     print(l[0:5])
# list()
"""====================================================================================================================="""

#28
# def list():
#     l =[]
#     for i in range(1,21):
#         l.append(i**2)
#     print(l[-5:])
# list()

#29
# def list():
#     l =[]
#     for i in range(1,21):
#         l.append(i**2)
#     print(l[5:])
# list()

#30
# def tup():
#     l=[]
#     for i in range(1,21):
#         l.append(i**2)
#     print(tuple(l))
# tup()

#31
# l= (1, 2, 3, 4, 5, 6, 7, 9, 10)
# print(l[0:5])
# print(l[-5:])

#32
# l= (1, 2, 3, 4, 5, 6, 7, 9, 10)
# s =[]
# for i in l:
#     if i%2==0:
#         s.append(i)
#     else:
#         pass
# print(tuple(s))

#33
# s = input()
# if s=="YES" or s=="Yes" or s=="yes":
#     print("YES")
# else:
#     print("NO")

#34
# l =[1,2,3,4,5,6,7,8,9,10]
# evennum = filter(lambda x: x%2==0,l)
# evennum = list(evennum) When you see <filter object at 0x0000013C37731660> printed out,
# it usually means that you have created a filter object but have not yet iterated over it or
# converted it to a list or another iterable form that you can inspect directly.
# print(evennum)

#35
# li = [1,2,3,4,5,6,7,8,9,10]
# squaredNumbers = map(lambda x: x**2, li)
# squaredNumbers = list(squaredNumbers) same as the above filter function
# print (squaredNumbers)

#36
# l =[1,2,3,4,5,6,7,8,9,10]
# evennum = filter(lambda x: x%2==0,l)
# evennum = list(evennum)
# squaredNumbers = map(lambda x:x**2,evennum)
# squaredNumbers =list(squaredNumbers)
# print(squaredNumbers)
# or
# evennum = map(lambda x: x**2, filter(lambda x: x%2==0, l))
# evennum =list(evennum)
# print(evennum)

#37
# even = filter(lambda x:x%2==0, range(1,21))
# even = list(even)
# print(even)

#38
# squaredNumbers = map(lambda x: x**2, range(1,21))
# squaredNumbers = list(squaredNumbers)
# print (squaredNumbers)

#39
# class American():
#     pass
# class Newyorker(American):
#     pass

# #40
# class Circle():
#     def __init__(self, radius):
#         self.radius= radius
#     def area(self,pi):
#         area = 2*pi*self.radius*self.radius
#         return area
# obj = Circle(8)
# print(obj.area(3.14))

# write the program to split the string without using split function

"""def split_function(string):

    sub_string=[]
    current_word =[]
    for char in string:

        if char == " ":
            sub_string.append("".join(current_word))
            current_word= []
        else:
            current_word.append(char)


    if current_word:

        sub_string.append("".join(current_word)) 
        return sub_string

print(split_function("hello im nandini, how do you do"))"""

