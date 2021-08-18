Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=12+3j
>>> (2+4j)+(5+3j)
(7+7j)
>>> (3+6j)-(4+5j)
(-1+1j)
>>> 7(3+4j)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    7(3+4j)
TypeError: 'int' object is not callable
>>> 7*(3+4j)
(21+28j)
>>> 7(3+4j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    7(3+4j)
TypeError: 'int' object is not callable
>>> (3+2j)*(5+j)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    (3+2j)*(5+j)
NameError: name 'j' is not defined
>>> (4+3j)*(2+1j)
(5+10j)
>>> (3+4j)=(3+4j)
SyntaxError: cannot assign to operator
>>> (3+4j)==(3+4j)
True
>>> x==(2+1j)
False
>>> x.conjugate()
(12-3j)
>>> (2+3J)/(3+2J)
(0.9230769230769231+0.38461538461538464j)
>>> ABS(3+2j)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    ABS(3+2j)
NameError: name 'ABS' is not defined
>>> abs(3+2j)
3.605551275463989
>>> import cmath
>>> cmath.phase (5+6j)
0.8760580505981934
>>> x.real
12.0
>>> x.imagen
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    x.imagen
AttributeError: 'complex' object has no attribute 'imagen'
>>> x.imag
3.0
>>> 