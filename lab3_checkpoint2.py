# Function will compute factorial of any positive number.
# Function will return value of 1 for any negative number
from math import factorial 

def xFactorial(x):
    if x>0:
      return factorial(x)
    else:
      return 1 
b=input("Type a number: ")
print "The factorial of", b, "is", xFactorial(b)

        


