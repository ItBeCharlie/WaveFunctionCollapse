# Charlie DeGennaro

import pygame
from random import random
import math

pygame.init()

globalAcc = -3
color = (255, 255, 255)
background = (0,155,50)
screenHeight = 800
screenWidth = 1400
card_spacing = 50

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


imageHeight = 182
imageWidth = 130
scaleFactor = 0.6 # Scale for normal size of image
viewingFactor = 1.5 # Scale for viewing the card

card_back_image = pygame.transform.scale(pygame.image.load('uno_assets_2d/PNGs/small/card_back_alt.png'), (int(scaleFactor*imageWidth), int(scaleFactor*imageHeight)))

players = []

def printList(list):
    for i in range(len(list)):
        print(list[i].str)

class Card:
    def __init__(self, value, color, special, image):
        self.value = value
        self.color = color
        self.special = special
        self.image = pygame.image.load(image)
        self.image_scaled = pygame.transform.scale(self.image, (int(scaleFactor*imageWidth), int(scaleFactor*imageHeight)))
        if(self.special == 'false'):
            self.str = self.color + str(self.value)
        else:
            self.str = self.color + self.special


class Deck:
    def __init__(self):
        self.cards = [
            Card(0, 'R', 'false', 'uno_assets_2d/PNGs/small/red_0.png'),
            Card(1, 'R', 'false', 'uno_assets_2d/PNGs/small/red_1.png'),
            Card(2, 'R', 'false', 'uno_assets_2d/PNGs/small/red_2.png'),
            Card(3, 'R', 'false', 'uno_assets_2d/PNGs/small/red_3.png'),
            Card(4, 'R', 'false', 'uno_assets_2d/PNGs/small/red_4.png'),
            Card(5, 'R', 'false', 'uno_assets_2d/PNGs/small/red_5.png'),
            Card(6, 'R', 'false', 'uno_assets_2d/PNGs/small/red_6.png'),
            Card(7, 'R', 'false', 'uno_assets_2d/PNGs/small/red_7.png'),
            Card(8, 'R', 'false', 'uno_assets_2d/PNGs/small/red_8.png'),
            Card(9, 'R', 'false', 'uno_assets_2d/PNGs/small/red_9.png'),
            Card(1, 'R', 'false', 'uno_assets_2d/PNGs/small/red_1.png'),
            Card(2, 'R', 'false', 'uno_assets_2d/PNGs/small/red_2.png'),
            Card(3, 'R', 'false', 'uno_assets_2d/PNGs/small/red_3.png'),
            Card(4, 'R', 'false', 'uno_assets_2d/PNGs/small/red_4.png'),
            Card(5, 'R', 'false', 'uno_assets_2d/PNGs/small/red_5.png'),
            Card(6, 'R', 'false', 'uno_assets_2d/PNGs/small/red_6.png'),
            Card(7, 'R', 'false', 'uno_assets_2d/PNGs/small/red_7.png'),
            Card(8, 'R', 'false', 'uno_assets_2d/PNGs/small/red_8.png'),
            Card(9, 'R', 'false', 'uno_assets_2d/PNGs/small/red_9.png'),
            Card(0, 'G', 'false', 'uno_assets_2d/PNGs/small/green_0.png'),
            Card(1, 'G', 'false', 'uno_assets_2d/PNGs/small/green_1.png'),
            Card(2, 'G', 'false', 'uno_assets_2d/PNGs/small/green_2.png'),
            Card(3, 'G', 'false', 'uno_assets_2d/PNGs/small/green_3.png'),
            Card(4, 'G', 'false', 'uno_assets_2d/PNGs/small/green_4.png'),
            Card(5, 'G', 'false', 'uno_assets_2d/PNGs/small/green_5.png'),
            Card(6, 'G', 'false', 'uno_assets_2d/PNGs/small/green_6.png'),
            Card(7, 'G', 'false', 'uno_assets_2d/PNGs/small/green_7.png'),
            Card(8, 'G', 'false', 'uno_assets_2d/PNGs/small/green_8.png'),
            Card(9, 'G', 'false', 'uno_assets_2d/PNGs/small/green_9.png'),
            Card(1, 'G', 'false', 'uno_assets_2d/PNGs/small/green_1.png'),
            Card(2, 'G', 'false', 'uno_assets_2d/PNGs/small/green_2.png'),
            Card(3, 'G', 'false', 'uno_assets_2d/PNGs/small/green_3.png'),
            Card(4, 'G', 'false', 'uno_assets_2d/PNGs/small/green_4.png'),
            Card(5, 'G', 'false', 'uno_assets_2d/PNGs/small/green_5.png'),
            Card(6, 'G', 'false', 'uno_assets_2d/PNGs/small/green_6.png'),
            Card(7, 'G', 'false', 'uno_assets_2d/PNGs/small/green_7.png'),
            Card(8, 'G', 'false', 'uno_assets_2d/PNGs/small/green_8.png'),
            Card(9, 'G', 'false', 'uno_assets_2d/PNGs/small/green_9.png'),
            Card(0, 'Y', 'false', 'uno_assets_2d/PNGs/small/yellow_0.png'),
            Card(1, 'Y', 'false', 'uno_assets_2d/PNGs/small/yellow_1.png'),
            Card(2, 'Y', 'false', 'uno_assets_2d/PNGs/small/yellow_2.png'),
            Card(3, 'Y', 'false', 'uno_assets_2d/PNGs/small/yellow_3.png'),
            Card(4, 'Y', 'false', 'uno_assets_2d/PNGs/small/yellow_4.png'),
            Card(5, 'Y', 'false', 'uno_assets_2d/PNGs/small/yellow_5.png'),
            Card(6, 'Y', 'false', 'uno_assets_2d/PNGs/small/yellow_6.png'),
            Card(7, 'Y', 'false', 'uno_assets_2d/PNGs/small/yellow_7.png'),
            Card(8, 'Y', 'false', 'uno_assets_2d/PNGs/small/yellow_8.png'),
            Card(9, 'Y', 'false', 'uno_assets_2d/PNGs/small/yellow_9.png'),
            Card(1, 'Y', 'false', 'uno_assets_2d/PNGs/small/yellow_1.png'),
            Card(2, 'Y', 'false', 'uno_assets_2d/PNGs/small/yellow_2.png'),
            Card(3, 'Y', 'false', 'uno_assets_2d/PNGs/small/yellow_3.png'),
            Card(4, 'Y', 'false', 'uno_assets_2d/PNGs/small/yellow_4.png'),
            Card(5, 'Y', 'false', 'uno_assets_2d/PNGs/small/yellow_5.png'),
            Card(6, 'Y', 'false', 'uno_assets_2d/PNGs/small/yellow_6.png'),
            Card(7, 'Y', 'false', 'uno_assets_2d/PNGs/small/yellow_7.png'),
            Card(8, 'Y', 'false', 'uno_assets_2d/PNGs/small/yellow_8.png'),
            Card(9, 'Y', 'false', 'uno_assets_2d/PNGs/small/yellow_9.png'),
            Card(0, 'B', 'false', 'uno_assets_2d/PNGs/small/blue_0.png'),
            Card(1, 'B', 'false', 'uno_assets_2d/PNGs/small/blue_1.png'),
            Card(2, 'B', 'false', 'uno_assets_2d/PNGs/small/blue_2.png'),
            Card(3, 'B', 'false', 'uno_assets_2d/PNGs/small/blue_3.png'),
            Card(4, 'B', 'false', 'uno_assets_2d/PNGs/small/blue_4.png'),
            Card(5, 'B', 'false', 'uno_assets_2d/PNGs/small/blue_5.png'),
            Card(6, 'B', 'false', 'uno_assets_2d/PNGs/small/blue_6.png'),
            Card(7, 'B', 'false', 'uno_assets_2d/PNGs/small/blue_7.png'),
            Card(8, 'B', 'false', 'uno_assets_2d/PNGs/small/blue_8.png'),
            Card(9, 'B', 'false', 'uno_assets_2d/PNGs/small/blue_9.png'),
            Card(1, 'B', 'false', 'uno_assets_2d/PNGs/small/blue_1.png'),
            Card(2, 'B', 'false', 'uno_assets_2d/PNGs/small/blue_2.png'),
            Card(3, 'B', 'false', 'uno_assets_2d/PNGs/small/blue_3.png'),
            Card(4, 'B', 'false', 'uno_assets_2d/PNGs/small/blue_4.png'),
            Card(5, 'B', 'false', 'uno_assets_2d/PNGs/small/blue_5.png'),
            Card(6, 'B', 'false', 'uno_assets_2d/PNGs/small/blue_6.png'),
            Card(7, 'B', 'false', 'uno_assets_2d/PNGs/small/blue_7.png'),
            Card(8, 'B', 'false', 'uno_assets_2d/PNGs/small/blue_8.png'),
            Card(9, 'B', 'false', 'uno_assets_2d/PNGs/small/blue_9.png'),
            Card(11, 'R', 'draw2', 'uno_assets_2d/PNGs/small/red_picker.png'),
            Card(11, 'G', 'draw2', 'uno_assets_2d/PNGs/small/green_picker.png'),
            Card(11, 'Y', 'draw2', 'uno_assets_2d/PNGs/small/yellow_picker.png'),
            Card(11, 'B', 'draw2', 'uno_assets_2d/PNGs/small/blue_picker.png'),
            Card(11, 'R', 'draw2', 'uno_assets_2d/PNGs/small/red_picker.png'),
            Card(11, 'G', 'draw2', 'uno_assets_2d/PNGs/small/green_picker.png'),
            Card(11, 'Y', 'draw2', 'uno_assets_2d/PNGs/small/yellow_picker.png'),
            Card(11, 'B', 'draw2', 'uno_assets_2d/PNGs/small/blue_picker.png'),
            Card(12, 'R', 'skip', 'uno_assets_2d/PNGs/small/red_skip.png'),
            Card(12, 'Y', 'skip', 'uno_assets_2d/PNGs/small/yellow_skip.png'),
            Card(12, 'G', 'skip', 'uno_assets_2d/PNGs/small/green_skip.png'),
            Card(12, 'B', 'skip', 'uno_assets_2d/PNGs/small/blue_skip.png'),
            Card(12, 'R', 'skip', 'uno_assets_2d/PNGs/small/red_skip.png'),
            Card(12, 'Y', 'skip', 'uno_assets_2d/PNGs/small/yellow_skip.png'),
            Card(12, 'G', 'skip', 'uno_assets_2d/PNGs/small/green_skip.png'),
            Card(12, 'B', 'skip', 'uno_assets_2d/PNGs/small/blue_skip.png'),
            Card(13, 'R', 'reverse', 'uno_assets_2d/PNGs/small/red_reverse.png'),
            Card(13, 'G', 'reverse', 'uno_assets_2d/PNGs/small/green_reverse.png'),
            Card(13, 'Y', 'reverse', 'uno_assets_2d/PNGs/small/yellow_reverse.png'),
            Card(13, 'B', 'reverse', 'uno_assets_2d/PNGs/small/blue_reverse.png'),
            Card(13, 'R', 'reverse', 'uno_assets_2d/PNGs/small/red_reverse.png'),
            Card(13, 'G', 'reverse', 'uno_assets_2d/PNGs/small/green_reverse.png'),
            Card(13, 'Y', 'reverse', 'uno_assets_2d/PNGs/small/yellow_reverse.png'),
            Card(13, 'B', 'reverse', 'uno_assets_2d/PNGs/small/blue_reverse.png'),
            Card(14, 'W', 'wild', 'uno_assets_2d/PNGs/small/wild_color_changer.png'),
            Card(14, 'W', 'wild', 'uno_assets_2d/PNGs/small/wild_color_changer.png'),
            Card(14, 'W', 'wild', 'uno_assets_2d/PNGs/small/wild_color_changer.png'),
            Card(14, 'W', 'wild', 'uno_assets_2d/PNGs/small/wild_color_changer.png'),
            Card(15, '4', 'wild', 'uno_assets_2d/PNGs/small/wild_pick_four.png'),
            Card(15, '4', 'wild', 'uno_assets_2d/PNGs/small/wild_pick_four.png'),
            Card(15, '4', 'wild', 'uno_assets_2d/PNGs/small/wild_pick_four.png'),
            Card(15, '4', 'wild', 'uno_assets_2d/PNGs/small/wild_pick_four.png'),
        ]

    def shuffle(self, num, deck):
        for j in range(num):
            for i in range(len(deck)-1):
                if random() >= 0.5:
                    temp = deck[i]
                    deck[i] = deck[i+1]
                    deck[i+1] = temp

    
class Game:
    def __init__(self):
        self.deck = Deck()
        self.drawPile = []
        self.drawPile.extend(self.deck.cards)
        self.discardPile = []

        # printList(self.drawPile)
        self.deck.shuffle(5000, self.drawPile)
        # printList(self.drawPile)

    def deal(self):
        # print(len(self.drawPile), len(self.discardPile))
        if len(self.drawPile) <= 0:
            self.reset()
        return self.drawPile.pop(0)

    def reset(self):
        self.drawPile.extend(self.discardPile)
        self.discardPile = []
        self.discardPile.insert(0, self.drawPile.pop(0))
        self.deck.shuffle(100, self.drawPile)
        for card in self.drawPile:
            if card.value == 14:
                card.color = 'W'
            if card.value == 15:
                card.color = '4'

    def discard(self, card):
        self.discardPile.insert(0, card)

    def topCard(self):
        return self.discardPile[0]

    def valid(self, card):
        if card.color == self.topCard().color:
            return True
        if card.value == self.topCard().value:
            return True
        if card.color == 'W' or card.color == '4':
            return True
        return False

class User:
    def __init__(self):
        self.hand = []

    def playCard(self, card): # Will change to be based off mouse position
        # temp = self.hand.index(card)
        temp = card
        return self.hand.pop(temp)

    def addCard(self, card):
        self.hand.extend([card])
        self.sortHand()

    def getCard(self, card):
        return self.hand[card]

    def sortHand(self):
        colors = [[], [], [], [], []]
        for i in range(len(self.hand)):
            color = self.hand[i].color
            if color == 'R':
                colors[0].extend([self.hand[i]])
            elif color == 'Y':
                colors[1].extend([self.hand[i]])
            elif color == 'G':
                colors[2].extend([self.hand[i]])
            elif color == 'B':
                colors[3].extend([self.hand[i]])
            else:
                colors[4].extend([self.hand[i]])

        self.hand = []

        for i in range(len(colors)):
            for j in range(len(colors[i])):
                for k in range(len(colors[i])-1):
                    if colors[i][k].value > colors[i][k+1].value:
                        temp = colors[i][k]
                        colors[i][k] = colors[i][k+1]
                        colors[i][k+1] = temp
            self.hand.extend(colors[i])
        


class Computer:
    def __init__(self):
        self.hand = []
        self.nums = [
            'numbers/badge-1.ico',
            'numbers/badge-2.ico',
            'numbers/badge-3.ico',
            'numbers/badge-4.ico',
            'numbers/badge-5.ico',
            'numbers/badge-6.ico',
            'numbers/badge-7.ico',
            'numbers/badge-8.ico',
            'numbers/badge-9.ico',
            'numbers/badge-10.ico'
        ]
        for i in range(len(self.nums)):
            self.nums[i] = pygame.transform.scale(pygame.image.load(self.nums[i]), (int(24), int(24)))

    def playCard(self):
        global game
        #First Pass - check for equal color (no special cards)
        for card in self.hand:
            # print(card.color, game.topCard().color, card.value)
            if card.color == game.topCard().color and card.value < 10:
                # print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
                return self.hand.pop(self.hand.index(card))

        #Second Pass - check for equal value (no special cards)
        for card in self.hand:
            if card.value == game.topCard().value and card.value < 10:
                return self.hand.pop(self.hand.index(card))

        #Third Pass - check for equal color (special cards)
        for card in self.hand:
            if card.color == game.topCard().color and card.value > 10:
                return self.hand.pop(self.hand.index(card))

        #Fourth Pass - check for equal value (special cards)
        for card in self.hand:
            if card.value == game.topCard().value and card.value > 10:
                return self.hand.pop(self.hand.index(card))

        #Fifth Pass = +4 wild cards
        for card in self.hand:
            if card.color == '4':
                self.chooseColor()
                return self.hand.pop(self.hand.index(card))

        #Sixth Pass = wild cards
        for card in self.hand:
            if card.color == 'W':
                self.chooseColor()
                return self.hand.pop(self.hand.index(card))

        #If no card can be selected, draw until a valid card is found
        self.addCard(game.deal())
        return self.playCard()    


    def chooseColor(self):
        global selectedColor
        global game

        colors = [0, 0, 0, 0]
        for i in range(len(self.hand)):
            color = self.hand[i].color
            if color == 'R':
                colors[0] += 1
            elif color == 'Y':
                colors[1] += 1
            elif color == 'G':
                colors[2] += 1
            elif color == 'B':
                colors[3] += 1

        maxNum = max(colors[0], colors[1], colors[2], colors[3])

        maxColors = []
        for i in range(len(colors)):
            if colors[i] == maxNum:
                maxColors.insert(0, i)

        rand = maxColors[int(random() * len(maxColors))]

        if rand == 0:
            selectedColor = 'R'
        elif rand == 1:
            selectedColor = 'Y'
        elif rand == 2:
            selectedColor = 'G'
        elif rand == 3:
            selectedColor = 'B'
        game.topCard().color = selectedColor
        
    def displayNum(self, position):
        global computerNumOffset
        if len(self.hand) > 9:
            cent(self.nums[9], (screenWidth/2 + computerNumOffset[0] + position[0], screenHeight/2 + computerNumOffset[1] + position[1]))
        else:
            cent(self.nums[len(self.hand)-1], (int(screenWidth/2 + computerNumOffset[0] + position[0]), int(screenHeight/2 + computerNumOffset[1] + position[1])))

    def addCard(self, card):
        self.hand.extend([card])


def initalizeGame():
    global players
    global game
    
    for _ in range(7):
        for i in range(len(players)):
            players[i].addCard(game.deal())
    game.discard(game.deal())

win = pygame.display.set_mode([screenWidth, screenHeight])
pygame.display.set_caption("UNO")

deck = Deck()

def cent(image, coords):
    coords = (coords[0] - image.get_rect().center[0], coords[1] - image.get_rect().center[1])
    win.blit(image, coords)

def centRect(rect, color, offset):
    rect.center = (screenWidth/2 + offset[0], screenHeight/2 + offset[1])
    pygame.draw.rect(win, color, rect)
    # win.blit(win, rect.center)
    
def doSpecial(card):
    global players
    global curDirection
    global curPlayer

    if card.special != 'false' and card.value != 14:
        if card.special == 'reverse':
            curDirection *= -1
        elif card.special == 'draw2':
            advanceTurn()
            players[curPlayer].addCard(game.deal())
            players[curPlayer].addCard(game.deal())
        elif card.special == 'skip':
            advanceTurn()
        elif card.value == 15:
            advanceTurn()
            players[curPlayer].addCard(game.deal())
            players[curPlayer].addCard(game.deal())
            players[curPlayer].addCard(game.deal())
            players[curPlayer].addCard(game.deal())




def advanceTurn():
    global curPlayer
    global curDirection
    global players

    curPlayer += curDirection
    curPlayer %= len(players)
    if curPlayer < 0:
        curPlayer = len(players)-1
    

def canPlayCard():
    global selected_card
    global players
    global game
    global selecting_color
    global selectedColor
    global advance_turn

    if game.valid(players[0].getCard(selected_card)):
        game.discard(players[0].playCard(selected_card))
        selectedColor = ''
        advance_turn = True
        if selected_card >= len(players[0].hand):
            selected_card = max(len(players[0].hand)-1, 0)
        if game.topCard().color == 'W' or game.topCard().color == '4':
            selecting_color = True
            advance_turn = False

def drawColorSelection():
    global hoveredColor
    centRect(pygame.Rect(screenWidth/2, screenHeight/2 + 50, 40, 40), RED, (-50, -100)) # Red
    centRect(pygame.Rect(screenWidth/2, screenHeight/2 + 50, 40, 40), YELLOW, (50, 0)) # Yellow
    centRect(pygame.Rect(screenWidth/2, screenHeight/2 + 50, 40, 40), GREEN, (-50, 100)) # Green
    centRect(pygame.Rect(screenWidth/2, screenHeight/2 + 50, 40, 40), BLUE, (-150, 0)) # Blue
    if hoveredColor == 'R':
        centRect(pygame.Rect(screenWidth/2, screenHeight/2 + 50, 80, 80), RED, (-50, -100)) # Red
    if hoveredColor == 'Y':
        centRect(pygame.Rect(screenWidth/2, screenHeight/2 + 50, 80, 80), YELLOW, (50, 0)) # Yellow
    if hoveredColor == 'G':
        centRect(pygame.Rect(screenWidth/2, screenHeight/2 + 50, 80, 80), GREEN, (-50, 100)) # Green
    if hoveredColor == 'B':
        centRect(pygame.Rect(screenWidth/2, screenHeight/2 + 50, 80, 80), BLUE, (-150, 0)) # Blue

def drawSelectedColor():
    global selectedColor
    if selectedColor == 'R':
        color = RED
    if selectedColor == 'Y':
        color = YELLOW
    if selectedColor == 'G':
        color = GREEN
    if selectedColor == 'B':
        color = BLUE
    centRect(pygame.Rect(screenWidth/2, screenHeight/2, 40, 40), color, (-50, 0))
    
def main():
    global hoveredColor
    global selected_card
    global selectedColor
    global selecting_color
    global draw_color_selection
    global curPlayer
    global curDirection
    global advance_turn
    global computerNumOffset
    global player
    global players
    global game

    game = Game()
    players = [User(), Computer(), Computer(), Computer()]
    curPlayer = 0
    hoveredColor = ''
    selectedColor = ''
    selecting_color = False
    draw_color_selection = False
    curDirection = 1
    advance_turn = False
    computerNumOffset = ((imageWidth*scaleFactor) / 2, (-1 * (imageHeight*scaleFactor)) / 2)

    player = players[0]


    player.sortHand()
    selected_card = 0

    initalizeGame()

    if game.topCard().special == 'wild':
        rand = int(random()*4)
        if rand == 0:
            selectedColor = 'R'
        if rand == 1:
            selectedColor = 'Y'
        if rand == 2:
            selectedColor = 'B'
        if rand == 3:
            selectedColor = 'G'
        game.topCard().color = selectedColor


    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and not selecting_color:
                if event.key == pygame.K_DOWN and curPlayer == 0:
                    tempCard = game.deal()
                    player.addCard(tempCard)
                    selected_card = player.hand.index(tempCard)
                if event.key == pygame.K_UP and len(player.hand) != 0 and curPlayer == 0: # Try to play card
                    canPlayCard()
                if event.key == pygame.K_LEFT:
                    selected_card -= 1
                    if selected_card < 0:
                        selected_card = len(player.hand)-1
                if event.key == pygame.K_RIGHT:
                    selected_card = (selected_card + 1)%len(players[0].hand)
            if event.type == pygame.KEYDOWN and selecting_color and curPlayer == 0:
                if event.key == pygame.K_DOWN:
                    hoveredColor = 'G'
                if event.key == pygame.K_UP: 
                    hoveredColor = 'R'
                if event.key == pygame.K_LEFT:
                    hoveredColor = 'B'
                if event.key == pygame.K_RIGHT:
                    hoveredColor = 'Y'
                draw_color_selection = True
                if event.key == pygame.K_RETURN:
                    selectedColor = hoveredColor
                    draw_color_selection = False
                    game.topCard().color = selectedColor
                    advance_turn = True

        # Computer's Turn
        if curPlayer != 0:
            pygame.time.delay(500)
            game.discard(players[curPlayer].playCard())
            advance_turn = True
        

        left_bound = ((screenWidth - len(player.hand)*card_spacing) / 2 ) + (card_spacing/2)
        
        win.fill(background)
        pygame.draw.rect(win, (0, 100, 200), ((50, 50), (screenWidth-100, screenHeight-100)))

        # Draw Players Hand
        # old_size = (int(scaleFactor*imageWidth), int(scaleFactor*imageHeight))
        for i in range(len(player.hand)):
            # picture = pygame.image.load(player.hand[i].image)
            # picture = pygame.transform.scale(picture, (65, 91)) # ORIG IMAGE SIZE: 130 x 182     SCALE IMAGE BY 1.4 ONLY
            if i != selected_card:
                cent(player.hand[i].image_scaled, (left_bound + (i*card_spacing), 600))
        if len(player.hand) != 0:
            cent(player.hand[selected_card].image_scaled, (left_bound + (selected_card*card_spacing), 580))
        if len(player.hand) > 25:
            cent(player.hand[selected_card].image_scaled, (screenWidth/2, 740))

        # Draw Discard Pile
        cent(game.topCard().image_scaled, (screenWidth/2 - 50, screenHeight/2))

        # Draw Draw Pile
        cent(card_back_image, (screenWidth/2 + 50, screenHeight/2))

        # Draw Computer Pile
        if(len(players) == 2 or len(players) == 3): # Player 2 across
            cent(card_back_image, (screenWidth/2, screenHeight/2 - 200))
            players[1].displayNum((0, -200))
        if(len(players) == 3): # Player 3 on left
            cent(card_back_image, (screenWidth/2 - 300, screenHeight/2))
            players[2].displayNum((-300, 0))
        if(len(players) == 4): # Player 4 on right
            cent(card_back_image, (screenWidth/2, screenHeight/2 - 200))
            cent(card_back_image, (screenWidth/2 - 300, screenHeight/2))
            cent(card_back_image, (screenWidth/2 + 300, screenHeight/2))
            players[1].displayNum((300, 0))
            players[2].displayNum((0, -200))
            players[3].displayNum((-300, 0))
        
        if draw_color_selection:
            drawColorSelection()

        if game.topCard().value < 14:
            selectedColor = ''
        
        if selectedColor != '':
            drawSelectedColor()
            game.topCard().color = selectedColor
            selecting_color = False

        if advance_turn:
            doSpecial(game.topCard())
            advanceTurn()
            advance_turn = False

        for p in players:
            if len(p.hand) == 0:
                print('Player', players.index(p), 'wins!')
                run = False

        pygame.display.update()


main()

pygame.quit()	





