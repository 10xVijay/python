

#slicing string
a="helol world"
print(a[2:5])
print(a[-5:-2])
print(a[-2:-1])        #first number allows variables to print whereas second number does not allow the variables to print

#modify string
b=" hey gommu "
print(b.upper())
print(b.lower())
print(b.strip())     #removes whitespace
print(b.replace("g","d"))    #replaces a word
print(b.split(","))      #splits the senetence

#format string
quantity=3
itemno=345
price=3400
myorder="i want to pay {2} rupees for {0} pieces for item {1} "
print(myorder.format (quantity,itemno,price))

#to escape the word in the string syntax
a="my name is \"gommu\" i am studing"
print(a)

#to escape statement in the syntax
# """"Code
# f\'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value"""

#string methods for code (built in functions)
"""Method	        Description
capitalize()        Converts the first character to upper case
casefold()	        Converts string into lower case
center()	        Returns a centered string
count()	            Returns the number of times a specified value occurs in a string
encode()	        Returns an encoded version of the string
endswith()	        Returns true if the string ends with the specified value
expandtabs()        Sets the tab size of the string
find()	            Searches the string for a specified value and returns the position of where it was found
format()	        Formats specified values in a string
format_map()        Formats specified values in a string
index()	            Searches the string for a specified value and returns the position of where it was found
isalnum()	        Returns True if all characters in the string are alphanumeric
isalpha()	        Returns True if all characters in the string are in the alphabet
isascii()	        Returns True if all characters in the string are ascii characters
isdecimal()	        Returns True if all characters in the string are decimals
isdigit()	        Returns True if all characters in the string are digits
isidentifier()      Returns True if the string is an identifier
islower()	        Returns True if all characters in the string are lower case
isnumeric()	        Returns True if all characters in the string are numeric
isprintable()   	Returns True if all characters in the string are printable
isspace()	        Returns True if all characters in the string are whitespaces
istitle()	        Returns True if the string follows the rules of a title
isupper()	        Returns True if all characters in the string are upper case
join()	            Joins the elements of an iterable to the end of the string
ljust()	            Returns a left justified version of the string
lower()	            Converts a string into lower case
lstrip()	        Returns a left trim version of the string
maketrans()	        Returns a translation table to be used in translations
partition()	        Returns a tuple where the string is parted into three parts
replace()	        Returns a string where a specified value is replaced with a specified value
rfind()	            Searches the string for a specified value and returns the last position of where it was found
rindex()	        Searches the string for a specified value and returns the last position of where it was found
rjust()	            Returns a right justified version of the string
rpartition()        Returns a tuple where the string is parted into three parts
rsplit()	        Splits the string at the specified separator, and returns a list
rstrip()	        Returns a right trim version of the string
split()	            Splits the string at the specified separator, and returns a list
splitlines()        Splits the string at line breaks and returns a list
startswith()        Returns true if the string starts with the specified value
strip()	            Returns a trimmed version of the string
swapcase()	        Swaps cases, lower case becomes upper case and vice versa
title()	            Converts the first character of each word to upper case
translate()	        Returns a translated string
upper()	            Converts a string into upper case
zfill()	            Fills the string with a specified number of 0 values at the beginning"""


#boolean value = to know the expresion is True or False in programing
print(10>9)
print(10==9)
print(10<9)
#as simple when we use if statement in python it returns True or False value
a=100
b=150

if b>a:
    print("b is greater then a")
else:
    print("b is less then a")
#as simple we use bool() function to evaluate the values 
# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty one.
print(bool("abc"))
print(bool(124))
print(bool(['apple','mango']))
print(bool(0))
print(bool(   ))
 
#Functions can Return a Boolean
#Python also has many built-in functions that return a boolean value, like the isinstance() function,
# which can be used to determine if an object is of a certain data type:
#check whether the object is an integer 
x = 200
print(isinstance(x, int))

