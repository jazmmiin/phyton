Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
if 5 > 2:
  print("Five is greater than two!")

  
Five is greater than two!
#This is a comment
print("Hello, World!")

Hello, World!
x = 5
y = "John"
print(x)
print(y)
SyntaxError: multiple statements found while compiling a single statement

x=5
y = "Jhon"
print (x)
5
print (y)
Jhon
x=5
y="Jhon"
print(type(x))
<class 'int'>
print (type(y))
<class 'str'>
x = "John"
# is the same as
x = 'John'
SyntaxError: multiple statements found while compiling a single statement
x="Jhon"
#is the same as
x='Jhon'
print (x)
Jhon
x, y, z="Banana", "Naranja", "Sandia"
print (x)
Banana
print (y)
Naranja
>>> print (z)
Sandia
>>> x=y=z= "Orange"
>>> print (x)
Orange
>>> print (y)
Orange
>>> print (z)
Orange
>>> fruits  = [banana, manzana, naranja]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    fruits  = [banana, manzana, naranja]
NameError: name 'banana' is not defined
>>> fruits  = ["banana", "manzana", "naranja"]
>>> x, y, z = fruits
>>> print (x)
banana
>>> print (y)
manzana
>>> print (z)
naranja
>>> x = "Hola "
>>> y = ":"
>>> z = ")"
>>> print (x,y,z)
Hola  : )
>>> x=5
>>> t=10
>>> print (x+t)
15
>>> x= "awesome"
>>> def myfunc():
...     print ("Phyton is "+x)
... 
...     
>>> my func()
SyntaxError: invalid syntax
>>> myfunc()
Phyton is awesome
