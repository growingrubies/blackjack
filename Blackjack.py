# -*- coding: utf-8 -*-
"""
Blackjack Game

Created on Sat Apr 18 18:32:49 2020

@author: Ruby
"""
"""
I would like to dedicate this script to anyone who has fallen through 
Rishi’s crack. No matter how bad things seem, you have a pick and a rope 
and you will climb your way out. You will be a stronger person after this.
"""
#imports
import numpy as np

#Create deck and score look-up: 
suite = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
ace = ['Ace']
nums = list(range(2, 11))
royal = ['Jack', 'Queen', 'King']
cards = ace + nums + royal
deck = [(str(card) + ' of ' + suit) for suit in suite for card in cards ]
points_suite = list(range(1, 11)) + [10, 10, 10]
points_deck = points_suite + points_suite + points_suite + points_suite
deck_dict = {deck[i] : points_deck[i] for i in range(len(deck))}

#Create functions:
def deal() : #Deal with replacement
    r1 = np.random.randint(0, 52)
    r2 = np.random.randint(0, 52)
    hand = [deck[r1], 
        deck[r2]]
    return hand

def is_natural_blackjack(score) :
        if sum(score) == 11 and sum([num == 1 for num in score]) > 0 :
            return True
        else : 
            return False       

def deal_round(hand) :
    r3 = np.random.randint(0, 52)
    card = deck[r3]
    hand.append(card)
    return hand

#Inititate game:
player = deal()
dealer = deal()
#d_total & p_total as list from iterations on dealer & player:
d_total = []
for card in dealer:
    d_total.append(deck_dict.get(card))
p_total = []
for card in player:
    p_total.append(deck_dict.get(card))
#Check for natural blackjack:
dnb = is_natural_blackjack(d_total)
pnb = is_natural_blackjack(p_total)

#First round:
print('-------------------------------------------------')
print('Your hand: ' + player[0] + ' and ' + player[1])
print('Your score is ' + str(sum(p_total)))
print('-------------------------------------------------')
print("Dealer's face up card: " + dealer[0])
if dnb == True and pnb == True :
    print('Game is a tie: dealer and player both have a natural blackjack')
elif dnb == True and pnb == False :
    print('Dealer wins with a natural blackjack')
elif dnb == False and pnb == True :
    print('Player wins with a natural blackjack')
else :
    print('There are no natural blackjacks')
print('-------------------------------------------------')
   
#Player rounds
draw = True

if draw == True:
    deal_round(player)
    p_total.append(deck_dict.get(player[-1]))
    print(player)
    print('Your score is now ' + str(sum(p_total)))

#Dealer's score
while 0 == 0 :
    if sum(d_total) >= 17 : #Manage scores above 17
        break
    elif sum([score == 1 for score in p_total]) > 0 : #Manage aces
        num_ace = sum([score == 1 for score in d_total])
        add_ace = 0
        d_total = sum(d_total) + 10*num_ace
        while add_ace <= num_ace:
            if 17 <= d_total <= 21 :
                print("The dealer's final score is " + str(d_total))
                break
            elif d_total < 17 :
                print('Score not between 17 and 21. Deal again...')
                dealer = deal_round(dealer)
                d_total.append(deck_dict.get(dealer[-1]))
                break
            else :
                d_total -= 10
                add_ace += 1
    else : #Manage score under 17 with no aces
        dealer = deal_round(dealer)
        d_total.append(deck_dict.get(dealer[-1]))
        print('New card dealt...')


#Calculate player's score:
if sum(p_total) <= 21 :
    if sum([score == 1 for score in p_total]) > 0 : #Manage aces
        num_ace = sum([score == 1 for score in p_total])
        add_ace = 0
        p_total = sum(p_total) + 10*num_ace
        while add_ace <= num_ace:
            if p_total <= 21 : #Catches highest possible score at or below 21
                print("Your final score is " + str(p_total))
                break
            else :
                p_total -= 10
                add_ace += 1
    else : #No aces, score at or below 21
        print('Your final score is ' + str(sum(p_total)))
else : #For scores over 21
    print('Your final score is ' + str(sum(p_total)))


#Game outcome:
print('Your hand:')
for card in player:
    print(card)
print('Your final score is ' + str(sum(p_total)))
print("The dealer's hand:")
for card in dealer:
    print(card)
print("The dealer's final score is " + str(sum(d_total)))
if sum(p_total) > 21 and sum(d_total) > 21 :
    print("It's a tie: everybody is bust.")
elif sum(p_total) == sum(d_total) :
    print("It's a tie: player and dealer have same score.")
elif sum(p_total) > 21 :
    print('Dealer wins: player is bust.')
elif sum(d_total) > 21 :
    print('Player wins: dealer is bust.')
elif sum(d_total) > sum(p_total) :
    print("Dealer wins with higher score.")
elif sum(p_total) > sum(d_total) :
    print("Player wins with higher score")


