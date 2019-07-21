# Mousetraps checkpoint 3 for COM S 104 lab 2
num = input("How many mousetraps? ")
resident = raw_input("Are you an Iowa Resident (y/n)? ")
if num <= 50:
    subtotal = num * 2.00
    if resident=="y":
        print "Subtotal: " + str(subtotal)
        tax=subtotal*0.05
        print "Tax: " + str(tax)
        total=tax+subtotal
        print "Total: " + str(total)
    else:
        print "Subtotal: " + str(subtotal)
        tax=subtotal*0.1
        print "Tax: " + str(tax)
        total=tax+subtotal
        print"Total: " + str(total)

else:
    first = 50 * 2.00
    extra = (num - 50) * 1.50
    subtotal = first + extra
    if resident=="y":
        print "Subtotal: " + str(subtotal)
        tax=subtotal*0.05
        print "Tax: " + str(tax)
        total=tax+subtotal
        print "Total: " + str(total)
    else:
        print "Subtotal: " + str(subtotal)
        tax=subtotal*0.1
        print "Tax: " + str(tax)
        total=tax+subtotal
        print"Total: " + str(total)
  







    
    
    
