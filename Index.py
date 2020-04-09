import pygame
from Class.Card import Card
from Class.descriptionCard import DescriptionCard
from Feature.MoveAction import *
from Class.Field.Field import Field
from Class.hand import Hand

pygame.init()
pygame.mixer.music.load("son.wav")
pygame.mixer.music.play()
volume = pygame.mixer.music.get_volume() #Retourne la valeur du volume, entre 0 et 1
pygame.mixer.music.set_volume(0.3) #Met le volume à 0.5 (moitié)

selected = None
lifepointJ1 = 100
lifepointJ2 = 100
manaJ1 = 50
manaJ2 = 50
goldJ1 = 10
goldJ2 = 10
graveyard = []
WIDTH = 1200
HEIGHT = 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()
pygame.display.set_caption('My Game')
fontDescription = pygame.font.SysFont("black", 36)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)
fieldImage = pygame.image.load("field.png").convert_alpha()
fieldSurface = fieldImage.get_rect(center=(600, 800))

field2Image = pygame.image.load("field2.png").convert_alpha()
field2Surface = field2Image.get_rect(center=(600, 200))

card1 = Card('Dragon Blanc aux yeux bleus')
card2 = Card('Magicien des ténèbres')
card3 = Card('Gobelin parvenu')
card4 = Card('Magicien des ténèbres')
card5 = Card('Gobelin parvenu')
card6 = Card('Dragon Blanc aux yeux bleus')
card7 = Card('Magicien des ténèbres')
card8 = Card('Gobelin parvenu')
card9 = Card('Dragon Blanc aux yeux bleus')
card10 = Card('Gobelin parvenu')

handJ1 = Hand()
fieldStatus = Field(lifepointJ1, lifepointJ2, goldJ1, goldJ2, manaJ1, manaJ2)
handJ1.drawCard([card1, card2, card4, card3, card10], fieldStatus, 'Player 1')

handJ2 = Hand()
handJ2.drawCard([card5, card6, card7, card8, card9], fieldStatus, 'Player 2')
fieldStatus.setHand(handJ1, handJ2)
field = []
descriptionZone = None
posSurface = (0, 0)
postImage = card1.__getattribute__('position')
is_running = True
clock = pygame.time.Clock()
timer = 0
currentPlayer = 'Player 1'
currentTourText = 'Tour de ' + currentPlayer
currentTour = fontDescription.render(currentTourText, True, (255, 255, 255))
currentTourRec = currentTour.get_rect(center=(600, 350))
pygame.time.set_timer(pygame.MOUSEBUTTONDOWN, 100)
while is_running:

    if currentPlayer == 'Player 1':
        hand = fieldStatus.__getattribute__('handJ1')
    elif currentPlayer == 'Player 2':
        hand = fieldStatus.__getattribute__('handJ2')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.MOUSEBUTTONDOWN and selected is not None and selected.__getattribute__(
                'owner') == currentPlayer:
            if event.button == 1:
                empty = fieldStatus.checkField(currentPlayer)
                target = detail(event.pos, field, hand)
                selectedPlace = selected.__getattribute__('field')
                if target is not None:
                    if target == selected:
                        if selectedPlace == False:
                            collision(event.pos, field, fieldStatus, currentPlayer)
                        elif empty == True and selected.__getattribute__('type') == 'Monster':
                            directAttak(selected, fieldStatus, currentPlayer)
                        elif selected.__getattribute__('type') == 'Action':
                            manageEffect(field, fieldStatus, currentPlayer, selected, graveyard)
                        selected = None
                        target = None
                    if target != selected is not None and target.__getattribute__('owner') != currentPlayer and selected.__getattribute__('type') == 'Monster' == \
                            target.__getattribute__('type'):
                        attakMonster(selected, target, graveyard, field, fieldStatus, currentPlayer)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                selected = detail(event.pos, field, hand)
                descriptionZone = DescriptionCard(selected, currentPlayer)
                timer = 0.001  # Start the timer.

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                manageGold(field, fieldStatus, currentPlayer)
                if currentPlayer == 'Player 1':
                    currentPlayer = 'Player 2'
                elif currentPlayer == 'Player 2':
                    currentPlayer = 'Player 1'
                currentTourText = 'Tour de ' + currentPlayer
                currentTour = fontDescription.render(currentTourText, True, (255, 255, 255))
                currentTourRec = currentTour.get_rect(center=(600, 350))
                fieldStatus.resetExhaust(currentPlayer)

    SCREEN.fill(BLACK)
    if fieldStatus.__getattribute__('winner') is None:
        SCREEN.blit(currentTour, currentTourRec)
        SCREEN.blit(field2Image, field2Surface)
        for card in fieldStatus.__getattribute__('handJ1').__getattribute__('cards'):
            SCREEN.blit(card.__getattribute__('sprite'), card.__getattribute__('rec'))
        for card in fieldStatus.__getattribute__('handJ2').__getattribute__('cards'):
            SCREEN.blit(card.__getattribute__('sprite'), card.__getattribute__('rec'))

        for card in field:
            SCREEN.blit(card.__getattribute__('sprite'), card.__getattribute__('rec'))
        SCREEN.blit(fieldImage, fieldSurface)
        # SCREEN.blit(rect_border, rect)
        if selected != None:
            SCREEN.blit(descriptionZone.__getattribute__('spriteDescription'),
                        descriptionZone.__getattribute__('rectDescription'))
            SCREEN.blit(descriptionZone.__getattribute__('spriteTitle'),
                        descriptionZone.__getattribute__('rectTitle'))
            SCREEN.blit(descriptionZone.__getattribute__('spriteImage'),
                        descriptionZone.__getattribute__('rectImage'))
            SCREEN.blit(descriptionZone.__getattribute__('spriteAttack'),
                        descriptionZone.__getattribute__('rectAttack'))
            SCREEN.blit(descriptionZone.__getattribute__('spriteGold'),
                        descriptionZone.__getattribute__('rectGold'))
        SCREEN.blit(fieldStatus.__getattribute__('spriteJ1'), fieldStatus.__getattribute__('recJ1'))
        SCREEN.blit(fieldStatus.__getattribute__('spriteJ2'), fieldStatus.__getattribute__('recJ2'))
        SCREEN.blit(fieldStatus.__getattribute__('spriteGoldJ1'), fieldStatus.__getattribute__('recGoldJ1'))
        SCREEN.blit(fieldStatus.__getattribute__('spriteGoldJ2'), fieldStatus.__getattribute__('recGoldJ2'))
        SCREEN.blit(fieldStatus.__getattribute__('spriteManaJ1'), fieldStatus.__getattribute__('recManaJ1'))
        SCREEN.blit(fieldStatus.__getattribute__('spriteManaJ2'), fieldStatus.__getattribute__('recManaJ2'))
        SCREEN.blit(fieldStatus.__getattribute__('spriteInstruction'), fieldStatus.__getattribute__('recIntruction'))
    else:
        SCREEN.blit(fieldStatus.__getattribute__('spriteWinner'), fieldStatus.__getattribute__('recWinner'))
    # SCREEN.blit(scoreJ2, scoreRect2)

    pygame.display.flip()

pygame.quit()
