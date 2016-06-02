import random
card_types=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
card_ranks = ['*H','*D','*C','*S']

def all_cards():
    temp_cards=[]
    cards=[]
    for i in range(0,13):
        for a in range(0,4):
            temp_cards.append(card_types[i]+card_ranks[a])
            a=+1
            #for loop 0..4 ends
        i =+1
        #for loop 0..13 ends
    cards = temp_cards
    return cards
    #def all_cards() ends here///

# print all_cards()

# def ask_card():
#     print "(i) Which card you want to ask?"
#     ask = raw_input("(i) You have %s >>" % Card_start.player_cards)
#     result = check_ask(ask)
#     if result == True:
#         print result
#         print ask
#     else:
#         print result
#         ask_card()
# #end of ask_card()
#
#
# def check_ask(ask):
#     ask_accepted = False
#     for a in range(0, len(Card_start.player_cards)):
#         if ask == Card_start.player_cards[a]:
#             ask_accepted = True
#             return ask_accepted
#         else:
#             a+=1
#     return ask_accepted
# #end of check_ask()

class Player():
    s=5

# class Bot():
#     a=3


# CARD_START CLASS BEGINS HERE

class Card_start():
    temp_cards = all_cards()
    print all_cards()
    random.shuffle(temp_cards)

    player_cards = temp_cards[0:7]
    bot_cards = temp_cards[7:14]

    for a in range(0, 7):
        temp_cards.remove(player_cards[a])
        a += 1

    for a in range(0, 7):
        temp_cards.remove(bot_cards[a])
        a += 1

    print "Player has got ", player_cards
    print "Bot has got", bot_cards
    print "All cards on the table", temp_cards
#class Card_start ends here
# ask_card()
