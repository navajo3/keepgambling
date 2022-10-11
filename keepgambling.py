import random
import time

loop = 1
loop2 = 1  # im too fucking stupid to make one loop co exist with 2 loop sequences

deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]               ## send help

currency = 40

cards = random.choice(deck)
op_cards = random.choice(deck)

game = True

def get_random_card():
    global randomcard
    randomcard = random.choice(deck)
    return 

def betting():
    global loop
    while loop == 1:
        bet = int(input("How much do you want to bet? "))    ## i was going to add an exception in the possibility of inputting a string however this is an inprobable scenario in a real game of blackjack
        if bet > currency:
            print("You dont have enough money to bet this amount!")
            continue
        elif bet <= 0:
            print("You cannot bet a negative amount!")
            continue
        else:
            loop = 0
            print("")
            return bet, loop

def cardcount():
    print("Current Card total: ", cards)
    print("")
    return

def hit_or_stand():
    global loop2, cards, randomcard
    while loop2 == 1:
        hit_or_stand = input("Hit or Stand? ").lower()
        print("")
        if hit_or_stand == "hit":
            cards += randomcard
            loop2 = 0
            return 
        elif hit_or_stand == "stand":
            loop2 = 0
            return
        else:
            print("Wrong Input")
            continue
        

def opcardrandom():
    global op_cards, possibility, loop2
    possibility = ["hit", "stand", "hit", "stand", "hit", "stand"]
    possibilityhs = random.choice(possibility)
    if possibilityhs == "hit":
        op_cards += random.choice(deck)
        loop2 = 1
        return op_cards
    else:
        return

def logic():
    global op_cards, cards
    if cards > op_cards:
        if cards > 21:
            print("You bust with,", cards, "while your opponent had", op_cards)
            return
        else:
            print("You win with", cards,"while your opponent had", op_cards)
            return
    elif cards < op_cards:
        if op_cards > 21:
            print("You win with", cards,"while your opponent busted with", op_cards)
        else:
            print("You lose with", cards,"while your opponent had", op_cards)
            return
    elif cards != op_cards:
        print("You tie, both players have", cards)      
        return                                                                              ## no idea if 50% of this is working as intended
    # elif cards > 21 and op_cards <= 21:
        print("You bust! You had", cards, " and your opponent had", op_cards)
        return
    # elif cards < 21 and op_cards >= 21:
        print("You win with ", cards," while your opponent busted with", op_cards)        # obsolete functions that do absolutely nothing useful bruh
        return
    # elif cards > 21 and op_cards > 21:
        print("You both busted with", cards, " and your opponent with", op_cards)
        return
    else:
        print("Error 0x4, cards are breaking the rules of the game.")

#def replay():   # wip
#    while loop == 0:
#        replay = input("Play again? (y/n): ").lower()
#        if replay == "y":
#            return
#        elif replay == "n":
#            print("you exit with", currency, " remaining.")
#            time.sleep(3)
#            break
#        else:
#            print("")

while game == True:
    betting()
    get_random_card()
    cardcount()
    opcardrandom()
    hit_or_stand()
    cardcount()
    opcardrandom()
    hit_or_stand()
    cardcount()
    opcardrandom()
    hit_or_stand()
    cardcount()
    logic()




