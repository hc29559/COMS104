# Plus Perfect Number
# All of the digits in the number raised to number of digits equals the number

def is_plus_perfect(n):
    number= str(n)
    num_digits=len(number)
    sum_of_digits= 0
    for b in number:
        sum_of_digits= sum_of_digits + int(b)**num_digits
    if sum_of_digits==n:
        return "a plus perfect number"
    else:
        return "not a plus perfect number"
 
        
a= int(input("Enter a positive number: "))
print is_plus_perfect(a)
