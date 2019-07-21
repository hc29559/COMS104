# If both are heads, player 1 wins
# If both are tails, player 2 wins,
# o therwise keep playing the game until one of the above happens 
from games import place_penny
from games import display_menu
print display_menu()
answer= raw_input("Enter your choice: ")
while answer!= "q":
    pn1= place_penny()
    print "Player 1 is: ", pn1
    pn2= place_penny()
    print "Player 2 is: ", pn2
    if pn1== "Heads" and pn2== "Heads":
        print "Player 1 wins the game"
        print display_menu()
        answer= raw_input("Enter your choice: ")
    elif pn1== "Tails" and pn2== "Tails":
        print "Player 2 wins the game"
        print display_menu()
        answer= raw_input("Enter your choice: ")
    else:
        while pn1!= pn2:
            print "Game continues..."
            pn1= place_penny()
            print "Player 1 is: ", pn1
            pn2= place_penny()
            print "Player 2 is: ", pn2
            if pn1== "Heads" and pn2== "Heads":
                print "Player 1 wins the game"
            else:
                if pn1== "Tails" and pn2== "Tails":
                        print "Player 2 wins the game"
        print display_menu()
        answer= raw_input("Enter your choice: ")
            
if answer== "q":
    print "Bye!"

        
