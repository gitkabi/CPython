# Strings are nothing but plain text inside the Double quotes.

("My name is Abhishek Kabi") 

print(type('My name is Abhishek Kabi')) # <class 'str'>

username = 'funnycoder'
password = 'funnysecret'

print(username)
print(password)

# Long-Strings      # They are represented by triple quotes

long_string = '''  
WOW
0 0
---

'''
print(long_string)

# How to add strings with spaces

first_name = 'Abhishek'
last_name = 'Kabi'
full_name = (first_name + ' ' + last_name)  # (' ') represents spaces in strings
print(full_name)

# String Concatenation  (Adding two strings together)

print('hello ' + 'World')

# Type conversion

print(type(int(str(100))))  # It will first convert it into string then into int type.

# Wht the above thing do is ->

a = str(100)                
b = int(a)
c = type(b)
print(c)

# Escape Sequence (\)

weather = "It's \"kinda\" sunny"
print(weather)

motivation = "Don't \ever \ quit"
print(motivation) 

# Adding tabs (\t) and newline (\n) in strings 

python = "\t Python is awesome"
print(python)

python =  'Python' '\nis awesome'
print(python)

# Formatted Strings (f and {})

name = 'Kabi'
age = '25'
print(f'Hi {name}.Your age is {age}')

a = 'cool'
b = 'trick'
print(f'Its a {a} {b}')

# Srting Indexes 

number = '0123456789'

#[start:stop:stepover]

print(number[5])
print(number[0:10])     # IT prints from 0-9
print(number[0:10:2])   # It skipes the number by 2
print(number[1:])       # It will start with 1 but print all numbr as default
print(number[:5])       # it will print till 5
print(number[::1])      # It will print all the values by default and steps over by 1
print(number[-1])       # In python the negative index starts from backside
print(number[-4])
print(number[::-1])     # It's a steppingover reverse of the string

# Immutability

numbers = '0123467'

numbers = '4'

print(number)           # It will give an error(Immutability) cz the format of string remains same once its printed