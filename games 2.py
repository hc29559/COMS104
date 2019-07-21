# both heads= player 1 wins
# both tails= player 2 wins

def place_penny():
    from random import randint
    r=randint(1, 10)
    if r%2==0:
        return "Heads"
    else:
        return "Tails"

def display_menu():
    print "###MENU###"
    print "p) Play the matching penny game"
    return "q) Quit"




