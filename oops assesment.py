# class Fileutility:
#     def __init__(self,filepath):
#         self.filepath = filepath
#
#     def read(self):
#         with open(self.filepath, 'r') as f:
#             content = f.read()
#         print(content)
#
#     def write(self,content):
#         with open(self.filepath, "w") as f:
#             f.write(content)
#             print(content)
#
#     def copy_file(self,filepath2):
#         with open(self.filepath, "r") as f:
#             content = f.read()
#             with open(filepath2, "w") as f:
#                 f.write(content)
#
#
# obj = Fileutility("C:\\Users\\mylar\\OneDrive\\Desktop\\python test nandini\\question 1.py")
# obj.read()
# obj = Fileutility("C:\\Users\\mylar\\OneDrive\\Desktop\\python test nandini\\question 1.py")
# obj.write("this is me")
# obj.copy_file( "C:\\Users\\mylar\\OneDrive\\Desktop\\python test nandini\\question 9.py")
import json


# class Mathoperations:
#     pi = 3.14
#     a = 5
#     b =6
#     @staticmethod
#     def addition():
#         print(Mathoperations.a+Mathoperations.b)
#         print(Mathoperations.pi + Mathoperations.b)
#     @staticmethod
#     def sub(a, b):
#         print(a-b)
#     @staticmethod
#     def mul(a, b):
#         print(a*b)
#     @staticmethod
#     def div(a, b):
#         print(a/b)
# calci = Mathoperations()
# calci.sub(8, 9)

# import math
# class Geometryhelper:
#     pi = 3.14
#     @staticmethod
#     def circle(r):
#         perimeter = 2*Geometryhelper.pi*r
#         area = Geometryhelper.pi*r**2
#         print("area is:", area, "perimeter is :", perimeter)
#     @staticmethod
#     def rectangle(l,b):
#         area = l*b
#         perimeter = 2*l*b
#         print("area is:", area, "perimeter is :",perimeter)
#     @staticmethod
#     def triangle(a,b,c):
#         s = a+b+c
#         area = (math.sqrt(s*(s-a)*(s-b)*(s-c)))
#         perimeter = a+b+c
#         print("area is:" ,area, "perimeter is :", perimeter)
#
# obj = Geometryhelper()
# obj.circle(6)
# # obj.triangle(8,7,5)
# import json
# # import yaml # i dont want to install yaml package
# class Parsing():
#     @staticmethod
#     def json_config(filepath):
#         with open(filepath, "r") as f:
#             return json.load(f)
#     @staticmethod
#     def yaml_config(filepath):
#         with open(filepath, 'w') as f:
#             return yaml.safe_load(f)
#
# obj = Parsing()
# # obj.yaml_config("C:\\Users\\mylar\\Downloads\\config.yaml")
# obj.json_config("C:\\Users\\mylar\\Downloads\\json.json")
# print(obj.json_config("C:\\Users\\mylar\\Downloads\\json.json"))
