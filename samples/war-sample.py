#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

# %% Generate deck of cards

deck = {}
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
cards = range(2, 15)
for suit in suits:
    for card in cards:
        if card == 11:
            deck["Jack of " + suit] = card
        elif card == 12:
            deck["Queen of " + suit] = card
        elif card == 13:
            deck["King of " + suit] = card
        elif card == 14:
            deck["Ace of " + suit] = card
        else:
            deck[str(card) + " of " + suit] = card

# %% Assign cards randomly to two players

deck_keys = list(deck.keys())
player1 = []
player2 = []
while len(deck_keys) > 0:
    player1.append(deck_keys.pop(random.randint(0, len(deck_keys)) - 1))
    player2.append(deck_keys.pop(random.randint(0, len(deck_keys)) - 1))

# %% PLAY WAR

round = 1
war = False
while len(player1) > 0 and len(player2) > 0:
    player1_cards_played = []
    player2_cards_played = []
    # draw cards
    print("Round " + str(round) + ". Player 1 " + str(len(player1)) + "-" + str(len(player2)) + " Player 2")
    player1_cards_played.append(player1.pop(0))
    player2_cards_played.append(player2.pop(0))
    print("      Player 1 draws " + player1_cards_played[-1])
    print("      Player 2 draws " + player2_cards_played[-1])

    # Evaluate cards
    if deck[player1_cards_played[-1]] > deck[player2_cards_played[-1]]:
        print("      Player 1 wins this round")
        player1.extend(player1_cards_played + player2_cards_played)
    elif deck[player2_cards_played[-1]] > deck[player1_cards_played[-1]]:
        print("      Player 2 wins this round")
        player2.extend(player1_cards_played + player2_cards_played)
    else:
        print("      WAR is declared!")
        war = True
    while war is True:
        # add three cards to each players pool
        draw = 4
        while draw > 0:
            player1_cards_played.append(player1.pop(0))
            player2_cards_played.append(player2.pop(0))
            if len(player1) == 0 or len(player2) == 0:
                break
            draw -= 1
        print("      Player 1 draws 3 cards and then " + player1_cards_played[-1])
        print("      Player 2 draws 3 cards and then " + player2_cards_played[-1])
        # compare fourth card
        if deck[player1_cards_played[-1]] > deck[player2_cards_played[-1]]:
            print("      Player 1 wins this round")
            player1.extend(player1_cards_played + player2_cards_played)
            war = False
        elif deck[player2_cards_played[-1]] > deck[player1_cards_played[-1]]:
            print("      Player 2 wins this round")
            player2.extend(player1_cards_played + player2_cards_played)
            war = False
        else:
            print("      WAR continues!")
    round += 1

