#-------------------String Functions--------------------
#----------------Assignment No 1------------------------
#------Muhammad Ahmad
#------Artificial Intelligence--------------------------
#------PIAIC72318---------------------------------------
#-------------------------------------------------------
#1---UPPER
name = "I'm Muhammad Ahmad & Father Name is Muhammad Hanif"
print(name.upper())

#2---TITLE
name="ahmad"
print(name.title())

#3---REPLACE
name="Hi I'm a Programmer"
print(name.replace("Programmer","Developer"))

#4---Find
name="Hi I'm a Programmer"
print(name.find("Programmer"))

#5---COUNT
name="Muhammad Ahmad"
print(name.count("M"))

#6---LOWER
name="MUHAMMAD AHMAD"
print(name.lower())

#7---FORMAT
name="Muhammad Ahmad"
age=21
print("Yyour Name is    {0} & Yyour Age is  {1}".format(name,age))

#8---LEN
name="Muhammad Ahmad"
print(len(name))

#9---STR
num1=50
num2=50
total=num1+num2 
print("SUM is " + str(total))

#10---CENTER
name="Muhammad Ahmad"
print(name.center(len(name)+8,"*"))

#11---CAPITALIZE
name= "muhammad ahmad"
print(name.capitalize())

#12---CASEFOLD
mame="B"
print(name.casefold())

#13---ENDWITH
Hi =" Python is Latest and Easy"
Hello= Hi.endswith("Easy")
print(Hello)

#14---EXPANDTABS
string= " Hi \t I've \t i5 3570"
res= string.expandtabs()
print(res)

#15---ENCODE
name="ThisisforEncoidng\pTesting"
res= name.encode()
print(res)

#16---INDEX
name="Ahmad"
print(name.index("ad"))

#17---ISALNUM
name="Muhammad Ahmad"
print(name.isalnum())

#18---ISALPHA
name="Muhammad AHmad"
print(name.isalpha())

#19---ISDECIMAL
name="2020"
print(name.isdecimal())

#20---ISDIGIT
name="2020"
print(name.isdigit())

#21---ISIDENTIFIER
name="FANTASTIC2020"
print(name.isidentifier())

#22---ISLOWER
name="mUhammad Ahmad"
print(name.islower())

#23---ISNUMERIC
name="2020"
print(name.isnumeric())

#24---ISPRINTABLE
name="Muhammad Ahmad"
print(name.isprintable())

#25---ISSPACE
name="MuhammadAhmad"
print(name.isspace())

#26---ISTITLE
name= "MUHAMMAD AHMAD"
print(name.istitle())

#27---ISUPPER
name="MUHAMMAD AHMAD"
print(name.isupper())

#28---JOIN
name="AHMAD"
Roll_N="718"
print(name.join(Roll_N))

#29---LJUST
name="Ahmad"
RNUM=7
print(name.ljust(RNUM))

#30---RJUST
name="Muhammad Ahmad"
RNUM=7
print(name.rjust(RNUM))

#31---SWAPCASE
name="This is Lower but Now Upper Case"
name="THIS IS UPPER"
print(name.swapcase())
print(name.swapcase())

#32---LSTRIP
name="          Muhammad Ahmad"
print(name.lstrip())

#33---RSTRIP
name="Muhammad Ahmad            "
print(name.rstrip())

#34---STRIP
name="FANTASTIC"
print(name.strip("FAN"))

#35---PARTITION
name="Muhammad AHMAD"
print(name.partition("AHMAD"))

#36---maketrans
dict = {"a": "123", "b": "456", "c": "789"}
string = "abc"
print(string.maketrans(dict))

#37---RPARTITION
name="Programming is Fun"
print(name.rpartition("is"))

#38---TRANSLATE
firstString = "abc"
secondString = "ghi"
thirdString = "ab"
string = "abcdef"
print("Original string:", string)
translation = string.maketrans(firstString, secondString, thirdString)

#39---RFIND
Inverted_String = 'Let it be, let it be, let it be'
result = Inverted_String.rfind('let it')
print("Substring 'let it':", result)

#40---RINDEX
Inverted_String = 'Let it be, let it be, let it be'
result = Inverted_String.rindex('let it')
print("Substring 'let it':", result)

#41---ISASCII
name="2020"
print(name.isascii())

#42---ZFILL
text = "program is Shit"
print(text.zfill(3))
print(text.zfill(2))
print(text.zfill(1))

#43---ADD
numbers = [2.5, 3, 4, -5]
numbersSum = sum(numbers)
print(numbersSum)
numbersSum = sum(numbers, 12)
print(numbersSum)

#44---DIR
name="a"
print(dir(name))

#45---FORMAT_MAP
name= {'x':'Muhammad','y':'Ahmad'}
print("{x} last name is {y}".format_map(name))

#46---CLASS
class Test:
    print("hello")

#47---CONTAINS
string= "North London is Red"
print("Red" in string  )

#48---DELATTER
class Coordinate:
    x= 10
    y= -5
    z= 0

point= Coordinate()

print('x= ', point.x)
print('y= ', point.y)
print('z= ', point.z)

delattr(Coordinate, 'z')

print("After deleting z attribute")
print('x= ', point.x)
print('y= ', point.y)

#49---GETATTR
class person:
    name= "Ashar"
    age= 22
person= Person()
print("Age is ", getattr(person, "age"))

#50---Getitem
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __getitem__(self,key):
        return getattr(self,key)

p = Person("AHMAD",21)
print (p["age"])

#51---HASH
vowels = ('a', 'e', 'i', 'o', 'u')

print('The hash is:', hash(vowels))

#52---init or _init_
class Student(object):

    def __init__(self, something):
        print("Init called.")
        self.something = something

    def method(self):
        return self.something 

my_object = Student('Setty')

#53---SUBCLASS
class Child():
	def __init__(self,name):
		self.name = name
class Student(Child): 
    #student is a subclass of child()
	def __init__(self,name,roll):
		self.roll = roll
		Child.__init__(self,name)
a = Child("xyz")
print(a.name)
b = Student("abc",17)
print(b.name)
print(b.roll)

#54---MOD
num1 = 6
num2 = 4
mod = num1%num2

print("Dividend : ", num1) 
print("Divisor : ", num2) 
print("Remainder : ", mod)

#55---MUL
num1=2
num2=2
Mul=num1*num2
print("Answer is ", Mul)

#56---NEW
# new() executes before init(). New() decides whether to use the init() method or not
class Sample(object):
    
    def __str__(self):
        return "SAMPLE"
class A(object):

    def __new__(cls):
        return Sample()
print(A())

#57--REDUCE: 
# reduce() stores the intermediate result and only returns the final summation value.

import functools
def mult(x,y):
    print("x=",x," y=",y)
    return x*y

fact=functools.reduce(mult, range(1, 4))
print ('Factorial of 4: ', fact)

#58---SIZEOFF

import sys 
#import sys in python is loading the module named sys into the current namespace so
#that you can access the functions and anything else defined within the module using the module name.
a = [1,2,3]
sys.getsizeof(a)

#58---SETATTR

class Person:
    name = 'AHMAD'
    
p = Person()
print('Before modification:', p.name)

# setting name to 'John'
setattr(p, 'name', 'Ahmad')

print('After modification:', p.name)

