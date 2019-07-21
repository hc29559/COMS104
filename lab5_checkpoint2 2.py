# computes the "n factorial"
# numbers must be >0
# factorial is multiplying all numbers through the specified number

def nFactorial(n):
    f=1
    for i in range (1, n+1):
        f= f*i
    return "The factorial is: " + str(f)
    


a=input("Enter a number greater than 0: ")
while a<=0:
    print "The number you entered is not greater than 0"
    a= input("Enter a number greater than 0: ")

print nFactorial(a)
