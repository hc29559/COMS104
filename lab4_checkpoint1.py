# re-write phone number to make it more readable
# add parentheses and dashes

def phoneNumberFormat(phone_number):
    num= str(phone_number)
    length=len((num))
    if length!=10:
        print "Error, a phone number must contain exactly 10 numbers"
        
    else:
        areaCode= (num[0:3])
        next3Digits= (num[3:6])
        last4Digits= (num[6:10])
    return "("+ areaCode + ")" + "-" + next3Digits + "-" + last4Digits

b= input("Enter your phone number with no spaces, paratheses, or other special characters: ")
print phoneNumberFormat(b) 
        
