# class Point:
#     def __init__(self,x,y):
#         self.x =x
#         self.y =y
#     def __str__(self):
#         return f"({self.x},{self.y})"
#     def __repr__(self):
#         return f"Point({self.x},{self.y})"
# obj = Point("nad","sad")
# print(obj)

class Employee:
    def __init__(self,string):
        self.string=string

    def __setitem__(self, key, value):
        self.string[key] = value

e = Employee({"dog": "broony", "age":2, "breed": "retriever"})
print(e.string)
e["dog"] ="tom"
print(e.string)
