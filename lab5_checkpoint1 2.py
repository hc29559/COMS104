# Counts how many times the letter "a" occurs in a phrase/sentence
# make sure it counts both upper and lower case "a"'s
# script will display when "a" or "A" occurs at what index

phrase= raw_input("Enter a phrase or sentence: ")
index= 0
print "The indexes of a are: "
for s in phrase:
    if s== "a" or s== "A":
        print s, "at index", index
    index+= 1

print count_a(phrase)
    
    
   
