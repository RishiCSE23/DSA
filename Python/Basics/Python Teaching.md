# 1. Introduction

* __Python__: High level programming language 
    * __High Level__: This is closer in interpreating to the the programmer.
    * __Programming Language__: Fomal way of a sequence of instructions to represent logical flow.
        * Flow in graphical format: Flowchart
        * Flow in a generic format: Algorithm 
        * Flow in a specific programming language: Program 
* Python is a _interpreted_ & partially _imparitive_ language
    * __Compilation__: Read the whole code and convert it into machine code (C,C++, Java\*, C#\*).
    * __Interpretation__: Read the code by every instrutions one-by-one while converting them into machine code (python, ruby). 

## 1.1. Variable

* Variable is a container of data. 
* Each variable varies is size based on the data it keeps.
* Every variable has a memory addresss on which it is kept in the computer memory. 
* Variable typing 
    * __Strongly/statically typed__: Variable's type must be specified before putting any data into it (C,C++, Java). 
    * __Weekly/Dynamicly typed__: Type of a variable is determined by the data put into it (Python, JavaScript). 
* Python is a dynamicly typed language
* Variable nomenclature 
    * First char of a variable must be a character or an underscore(_) 
    * length of the variable name is limited to 128 char. 


```python
# variable example   <--- comment 

a=10   # assigning 10 into a 
b=None # declaring b as a empty variable 
```


```python
# testing type of a variable 
type(a)
```




    int




```python
type(b)
```




    NoneType




```python
a=10.0
```


```python
type(a)
```




    float



### 1.1.1 Common datatypes


```python
a = 10     # integer (whole number)
b = 10.2   # floating-point (fraction number)
c = "abcd" # string (character sequence)
```


```python
print(type(a))
print(type(b))
print(type(c))
```

    <class 'int'>
    <class 'float'>
    <class 'str'>
    


```python
# print example 
print('hello world')  # telling the program to print somethingon the screen 
```

    hello world
    


```python
# format string 
print(f'type of {a} is {type(a)}.')
print(f'type of {b} is {type(b)}.')
print(f'type of {c} is {type(c)}.')
```

    type of -10 is <class 'int'>.
    type of -10.2 is <class 'float'>.
    type of abcd is <class 'str'>.
    


```python
# use of both "", '' in strings
print('I am a programmer...')
print("I'm a programmer...")
print('he said "I am a programmer"')
```

    I am a programmer...
    I'm a programmer...
    he said "I am a programmer"
    

### 1.1.2. Python Specific Data types
* None = Nothing 
* Boolean = True/False 
* Abstact data type (ADT): Data-structures, unlike variables they represent a collection 
    * List: `[1,2,3,3,12,1.6,'abc']`   is a mutable collection 
    * Tuple: `(1,2,3,3,12,1.6,'abc')`  is a immutable collection 
    * Set: `{1,2,3,12}`  is a mutable collection of unique 
    * Dictionary: `{'name':'Puja' , 'age':28}`  is key-value map 


```python
c = None  # nothing 
d = True  # or False  

lst = [1,2,3,3,12,1.6,'abc']  # mutable collection where redundancy is allowed 
tup = (1,2,3,3,12,1.6,'abc')  # immutable collection where redundancy is allowed 
st = {1,2,3,3,12,1.6,'abc'}   # mutable collection where redundancy is NOT allowed 
stu_1 = {'name':'Puja Chatterjee', 
         'age':28, 
         'qualification':'PG', 
         'height':5.2,
         'year_of_exp':5.2,
         'unit':'cm'}
```


```python
print(f'type of {lst} is {type(lst)}')
print(f'type of {tup} is {type(tup)}')
print(f'type of {st} is {type(st)}')
```

    type of [1, 2, 3, 3, 12, 1.6, 'abc'] is <class 'list'>
    type of (1, 2, 3, 3, 12, 1.6, 'abc') is <class 'tuple'>
    type of {1, 2, 3, 1.6, 'abc', 12} is <class 'set'>
    


```python
name= stu_1['name']    # accessing the value of the stu_1 by the key 'name'  
height=stu_1['height'] # stu_1's height
unit=stu_1['unit']

print(f'The student {name} is {height}{unit} tall')
```

    The student Puja Chatterjee is 5.2cm tall
    


```python
print(f"The student {stu_1['name']} is {stu_1['height']}{stu_1['unit']} tall")
```

    The student Puja Chatterjee is 5.2cm tall
    

## 1.2. Operators

* Used for arithmatic and logial calculation 
* Arithmatic Operators

| Operator | Meaning | Syntax |
|---|---|---|
| =  | Assignemnt | `a=b`|
| +  | Addition | `a+b`|
| -  | Subtraction | `a-b`|
| *  | Multiplication | `a*b`|
| /  | Division | `a/b`|
| %  | Modulus  | `a%b`|
| **  | Exponent | `a**b`|
| //  | int division | `a//b`|
| +=  | add and assign | `a+=b => a = a+b`|

* Logical Operators (output is boolean)

| Operator | Meaning | Syntax |
|---|---|---|
| <   | Less than | `a<b`|
| <=  | Less than or equals to | `a<=b`|
| >   | Greater than | `a>b`|
| >=  | Less than or equals to | `a>=b`|
| ==  | Equality | `a == b`|
| !=  | Inequality | `a != b`|
| and | if both are True  | `a and b`|
| or  | if eather of them are true  | `a or b`|
| not | negation  | `not a`|
| in  | membership check | `a in b`|

* Bitwise operator

| Operator | Meaning | Syntax |
|---|---|---|
| &  | bitwise AND | `a&b`|
| |  | bitwise OR | `a|b`|
| ^  | bitwise XOR | `a&b`|
| ~  | bitwise NOT | `~a`|
| << | bitwise LEFT SHIFT | `~a`|
| >> | bitwise LEFT SHIFT | `~a`|


```python
C=5+6   # high level (5+6)
print(C)

print(
"""
LOAD A,5  # LOAD A = opcode (what to do?) , 5 = operand (on what to do?) 
LOAD B,6
ADD A,B
STO C
""")
```

    11
    
    LOAD A,5  # LOAD A = opcode (what to do?) , 5 = operand (on what to do?) 
    LOAD B,6
    ADD A,B
    STO C
    
    


```python
# Arithmatic
a=10
b=6

print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b}')
print(f'{a}//{b}={a//b}')
print(f'{a}**{b}={a**b}')
print(f'{a}%{b}={a%b}')
a+=b
print(a)
```

    10+6=16
    10-6=4
    10*6=60
    10/6=1.6666666666666667
    10//6=1
    10**6=1000000
    10%6=4
    16
    

### 2.1.1. Truth value evaluation

* Any non-zero number is True
* 0 is False
* None is False
* Empty String is False
* Non-empty string is true 
* Any empty ADT is False
* Any non-empty ADT is True 

```
y=bool(x)
print(y)
```


```python
# Logical
print(bool(3))  # true
print(bool(-2)) # true
print(bool(0))  # false
print(bool(None)) # false
print(bool('')) #false
print(bool( [] ))
print(bool( () ))
print(bool( {} ))
print(bool('a')) #true
print(bool( [1] ))
print(bool( (1) ))
print(bool( {1} ))
```

    True
    True
    False
    False
    False
    False
    False
    False
    True
    True
    True
    True
    


```python
a=5
b=6
c=[]
```


```python
a<b  # is a less than b?
```




    True




```python
a <= b 
```




    True




```python
a <= a
```




    True




```python
a < a
```




    False




```python
a > b
```




    False




```python
a >= b
```




    False




```python
a == b  
```




    False




```python
a != b   # is a not equals to b?
```




    True




```python
bool(a and b)
```




    True




```python
bool(a and c)
```




    False




```python
bool(a or c)
```




    False




```python
bool(not c)
```




    True



Membership means: $x\in L$


```python
lst1=[1,2,3,4]
x=2
y=6
x in lst1
```




    True




```python
y not in lst1
```




    True



```
	      8421 	
a=13   :  1101        
b=6    :  0110
-------------------
a&b    :  0100 (4)
a|b    :  1111 (15)
a^b    :  1011 (11)
a<<2   :  110100 (52)
a>>2   :  11 (3)


			    531 = 5*2^2+ 3*2^1+ 1*2^0

                    5  4  3  2  1  0 <-- i
		            32 16 8  4  2  1 <-- 2^i
                    ----------------
                          0  1  0  0
      
 a b a&b a|b a^b
 0 0  0   0   0
 0 1  0   1   1 
 1 0  0   1   1
 1 1  1   1   0


a=13 = 1101
   
a<<1 = 16 8 4 2 1
       1  1 0 1 0 = 16+8+2 = 26 

       8421 
a>>1 = 0110
       4+2 = 6  = 13//2 

13<<1 = 13*2^1 = 13 * 2
13<<2 = 13*2^2 = 13 * 4


a<<n == a*(2**n)
a>>n == a//(2**n)
```


```python
# bitwise 
a=13
b=6
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(a>>2)
```

    4
    15
    11
    52
    3
    


```python

```
