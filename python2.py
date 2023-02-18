print("*"*10)
# print * ten times

print('Nikhil Mahajan')
# '' can also be used for string

price=10
# no need to pre define type of variable

age = input('what is ur age?')
# by default input is of type string

age_in_int = int(age)
# convert age to integer

print(f"my age is {age_in_int}")
# formated string 

print(type(age))

course = '''
hello,
This is allien trying to contact humans
be aware
'''
# Multi Line strings 

print(course)

str = 'python for beginners'
# str[-2] === second character from end === r
# str[-1] === first character from end === s

# str[1:4] === yth === character at index 4 is excluded
# len(str) === length of str === 20

# 'python' in str === return boolean === true


# 10/3 === 3.333333333
# 10//3 === 3
# 10**3 === 10 to the power 3 === 1000

is_hot = True
is_cold = False
# here T in True is in upper case

if is_hot:
    print("It's hot")
    print("Take cap with u")
elif is_cold:
    print("Its cold")
    print("Wear sweater")
else :
    print("its lovely day")

# && === and 
# || === or
# ! === not

if (3!=4 and not 0) or not 1 :
    print("Hello")

i = 0
while i<5 :
    print(i)
    if i==3:
         break  
    i+=1
else :
    print('''This is else statement of while and executed only if i<5 condition 
    gets false during execution of while loop
    As above loop break due to break statement so this statement
    will not be executed''')

# array === list
# object === dictionaries

names_list = ["John","smith","dhoni","Keshav"]

for character in 'Python':
    print(character)

for name in names_list:
    print(name)
# names_list[1:3] === ["smith","dhoni"] === index 3 is excluded

for x in range(1,4):
    print(x)
# 1,2,3 is printed === 4 is excluded

if "dhoni" not in names_list:
    names_list.append("dhoni")

# destructuring
coordinates = (1,2,3)
x,y,z = coordinates
# x==1 , y==2 , z==3

customer = {
    "name":"John smith",
    "age":27,
    "isVerified": True
}

# customer["name"] === John smith
customer['balance']=1000


# functions

def greetUser(index,name,greet):
    print(f'{greet} , {name} Have a nice day')

greetUser(0,"John","Hello")
greetUser(1,greet="Hiii",name="Smith")


class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y  
        # self refers to object of class Point for which this constructor is called
        # def __init__ is way to define constructor in python
    def distance(self,point):
        dist = ((self.x-point.x)**2 + (self.y-point.y)**2)**0.5
        print(f"Distance b/w points are {dist}")


point1 = Point()
point2 = Point(1,1)
point2.distance(point1)
# Functions in class are called methods


# ----------------------------------------------


# import convertors 
# convertors.kg_to_lbs(20) === calling the function in convertors module
 
# from convertors import kg_to_lbs
# kg_to_lbs(20) === importing the specific function from convertors module and using 
#                   it directly 


# import openpyxl as xl
# from openpyxl.chart import BarChart,Reference