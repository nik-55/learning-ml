# import docx
# pip install python-docx
# pip uninstall python-docx
# C:\Python310\Lib --> inBuilt modules are present here
# C:\Python310\Lib\site-packages --> external modules are present here
# pip is a package manager which is preinstalled in python3

# def translate(phrase):
#     translation = ""
#     for character in phrase:
#         if character in "AEIOUaeiou":
#             if character.islower():
#                 translation += 'g'
#             else:
#                 translation += 'G'
#         else:
#             translation += character

#     return translation


# print(translate(input()))

# try:
#     number = int(input())
#     print(number)
#     value = 10/0
# except ValueError:
#     print("Hey enter a number")
# except ZeroDivisionError as mssg:
#     print(f"division by zero error, message : {mssg}")
# except:
#     print("Accept everything")

# employee_file = open("employee.txt", "r")
# print(employee_file.readable())
# print(employee_file.read())
# employee_file.close()

# inbuilt modules
# external modules

# class Student:
#     def __init__(self, name):
#         self.name = name


# leave two line after class
# student1 = Student("nikhil")
# student1 is a object
# print(student1.name)

# class IndianChef(Chef):
# IndianChef class inherit Chef class
