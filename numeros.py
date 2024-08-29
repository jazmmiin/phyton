Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#int
x= 983839
z= 1
y= -903292
print (type(x))
<class 'int'>
print (type(y))
<class 'int'>
print(type(z))
<class 'int'>
#float
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
SyntaxError: multiple statements found while compiling a single statement
x= 1.10
y=1.0
z= -35.59
print(type(x))
<class 'float'>
print(type(y))
<class 'float'>
print(type(z))
<class 'float'>
>>> x=35e10
>>> print (type(x))
<class 'float'>
>>> x= 3+5j
>>> y=7000000000000000000000000000000000000000000000000000000000000000000000000000000000000j
>>> z=-93475j
>>> print(type(x))
<class 'complex'>
>>> print(type(y))
<class 'complex'>
>>> print(type(z))
<class 'complex'>
>>> x= 1 #int
>>> y= 2.8 #float
>>> z= 567j #complex
>>> #convertir int en float
>>> a =float(x)
>>> #convertir float en int
>>> b =int(y)
>>> #convertir int en complex
>>> c =complex(z)
>>> print(type(x))
<class 'int'>
>>> print (a)
1.0
>>> print (b)
2
>>> print (c)
567j
>>> print (type(a))
<class 'float'>
>>> print (type(b))
<class 'int'>
>>> print (type(c))
<class 'complex'>
>>> #Nota: No puede convertir números complejos en otro tipo de número.
>>> import random
>>> print(random.randrange(1, 10))
5
>>> 
