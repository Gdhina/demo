# Primitive Datatypes
# Represents single value
# Minimum set of operations 
# No methods, only functions
# Immutable (Cannot be changed after decalaration)
# int , float(decimal), string("sdg",'sdg123',"123"), Boolean (True, False)

# Variables are used to store the values in a program (x = 55)
# Starts with alphabet, use underscore instead of spaces, can be alphanumeric
# cannot start with number, cannot be a keyword(int,float,str,for) (not allowed 1name , 1class) (allowed[name1])
# Case sensitive (name = "Raja") (print(Name)) name != Name

a = 11 # programmer defined input
print(a)
print("Hello Everyone")
print(type(a)) # <class 'int'>
print("The value of a is",a)
print(f"{a} is the value of a") # f-string formatting

# user defined input
num = int(input("Enter your number: ")) # input is a function and the default datatype is str
print(type(num))

decimal = float(input("Enter a float: "))
print(f"decimal value is {decimal} and the datatype is {type(decimal)}")

print(f"Converted integer for decimal value is {int(decimal)}")

str_num = input("Enter a number that can be converted into int: ") # class str
print(f"The type of a str_num is {type(str_num)}")
print(f"Converted integer for str_num value is {int(str_num)}") 
# if the input is not a number, it will throw an error

# Boolean
is_admin = True
print(f"The type of is_admin is {type(is_admin)}") # <class 'bool'>

str1 = "Hello"
print(str1)
# Index starts from zero
print(str1[0]) # H
print(str1[4])
print(len(str1))
# slicing 
str2 = "Hello Everyone"
# [start: stop : step] index of the values
# from backwards, starts from -1  
print(str2[:]) # starts from zero and till n
# step is optional, default is +1
print(str2[0:5])
print(str2[6:])
print(str2[6:11])

# relation between start and step is +
print(str2[-1:-4:-1])
str3 = "racecar" # Palindrome
print(str3[::-1])

# Arithmetic operators
# + (addition), - (subtraction), * (multiplication), ** (exponential)
# Division : 3 categories 
# normal division / => returns the quotient
# floor division // => returns the quotient without the decimal part
# modulus % => returns the remainder 
print(11/3) # 3.6666666666666665
print(10//3) # 3
print(10%3) # 1 remainder

print(-15//2)
print(123%10)
print(123//10)

# comparison operators
# <, >, <=, >=, == compare that values are same,
# != compare that values are not same print(11 != 11)
# returns the bool3ean value (T/F)


# logical operators
# and, or, not
# and => both the conditions are true
# or => either the condition should be true
# not => negates the boolean value(T/F)
print(10>5 and 10<=15)
print(10>5 or 10==15)
print(not(10>5))

# identity operators
# is, is not
a=11
b=22
# assumptions made by the programmer
print(a is b)
print(a is not b)

# membership operators - (string, non-[primitive datatypes])
# in, not in
print(1 not in [1,3,5,78,8])
print(12 in [1,2,3,4,5])






























