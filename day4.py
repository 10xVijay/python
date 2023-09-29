
#code for single value for multiple veriables
x=y=z= "books"

print(x,y,z)
# print(y)
# print(z)


#code for unpaking veriables

fruits = ["oregne","banana","apple"]    

x,y,z= fruits

print(x)
print(y)
print(z)

#globle veriable concept you can creat veriable inside or outside of fuction 

#example -

v = "awesome"

def myfunc():

    print("python is",v)

myfunc()

#using local and globle veriable in one function 


s = "awesome"
def myfunc():
    s= "fantastic"
    print ("python is ",s)

myfunc()
print("python is ",s)


#the global keyword to use globle veriable inside the function 

def myfunc():
    global r
    r = "osm"

myfunc()
print("python is ", r)






