"""COMP 110 Exercise 01, Numeric Operators"""
__author__  = "730396438"

x: str = input("Left-hand side: ")
y: str = input("Right-hand side: ")

num_1 = int(x)
num_2 = int(y)

print(x + ' ** ' + y + " is " + str(num_1 ** num_2))
print(x + ' / ' + y + " is " + str(num_1 / num_2))
print(x + ' // ' + y + ' is ' + str(num_1 // num_2))
print(x + ' % ' + y + ' is ' + str(num_1 % num_2))