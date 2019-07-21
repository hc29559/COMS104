# Recall combination order doesn't matter
# Recall permutation order DOES matter

from lab3_checkpoint2 import xFactorial
n=input("Total number of elements: ")
r=input("Numer of elements to be selected: ")

if n>=r:
    a=xFactorial(n)
    b=xFactorial(n-r)
    c=xFactorial(r)
    permutation=a/b
    combination=a/(c*b)
    print "You have", permutation, "permutations and", combination, "combinations to select!"
else:
    print "Sorry, you cannot select",r,"from a collection of",n,"elements!"
