# Fundamental Data Types

# int and float

print(type(6)) 
print(type(2 + 7))
print(type(2 - 7))
print(type(2 * 7)) 

print(type(2 / 7))      # Floating Number (0.285) 
print(type(0.287))      # Floating number
print(type(20 + 1.2))   # Floating number (It converts the value 20+1.2 to float)
print(type(4.0 + 6.0))  # Floating number (10.0)

print(2 ** 3)           # (8) Power 
print(5 // 4)           # (1) Dividend (Rounds off to closest integer) 
print(3 // 4)           # (0)
print(5 % 4)            # (1) Modulus (Gives te remaining reminder)

# Math funtions

print(round(3.3))       # (3) Rounds to nearest integer
print(round(3.9))       # (4)
print(abs(-20))         # (20) Absolute Value 

# Operator precedence

print(20 + 4 * 2)
print((20 + 4) + 2 ** 2) # Different  Operators are (), **, */, + -

# Binary and Complex numbers

print(bin(5))           # (0b101) Binary of 5 is 101
print(int('0b101', 2))  # (5) Converting  binary to integer

complex                 # (Real + imag * 1j) where imag is 0