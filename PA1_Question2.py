# If number is not divisible by 4, not a leap year
# If number is divisible by 100 but not by 400, not a leap year
# If number is divisible by 100 and 400, leap year
# If number isn't divisible by 100 but is divisible by 4, it's a leap year

year=input("Enter a year greater than 100: ")
if year%4!=0:
 print year, "is not a leap year!"
elif year%100==0 and year%400!=0:
 print year, "is not a leap year!"
if year<=100:
 print "Error: Year is less than or equals to 100"
elif year%100==0 and year%400==0:
 print year, "is a leap year!"
elif year%100!=0 and year%4==0:
 print year, "is a leap year!"
