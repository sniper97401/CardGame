import pygame


class Field:
    player = None
    monstersJ1 = [
        [0, (433, 800), 0],
        [0, (517, 800), 0],
        [0, (603, 800), 0],
        [0, (686, 800), 0],
        [0, (767, 800), 0],
    ]

    monstersJ2 = [
        [0, (433, 200), 0],
        [0, (517, 200), 0],
        [0, (603, 200), 0],
        [0, (686, 200), 0],
        [0, (767, 200), 0],
    ]

    actionsJ1 = [
        [0, (433, 873), 0],
        [0, (517, 873), 0],
        [0, (603, 873), 0],
        [0, (686, 873), 0],
        [0, (767, 873), 0],
    ]

    actionsJ2 = [
        [0, (433, 130), 0],
        [0, (517, 130), 0],
        [0, (603, 130), 0],
        [0, (686, 130), 0],
        [0, (767, 130), 0],
    ]

    fieldHandJ2 = [
        [0, (433, 50), 0],
        [0, (517, 50), 0],
        [0, (603, 50), 0],
        [0, (686, 50), 0],
        [0, (767, 50), 0],
    ]

    fieldHandJ1 = [
        [0, (433, 940), 0],
        [0, (517, 940), 0],
        [0, (603, 940), 0],
        [0, (686, 940), 0],
        [0, (767, 940), 0],
    ]

    lifepointJ1 = None
    lifepointJ2 = None
    goldJ1 = None
    goldJ2 = None
    manaJ1 = None
    manaJ2 = None
    handJ1 = None
    handJ2 = None
    spriteJ1 = None
    recJ1 = None
    spriteJ2 = None
    recJ2 = None
    font = None
    spriteGoldJ1 = None
    spriteGoldJ2 = None
    recGoldJ1 = None
    recGoldJ2 = None
    spriteManaJ1 = None
    spriteManaJ2 = None
    recspriteManaJ1 = None
    recspriteManaJ2 = None
    spriteInstruction = None
    recInstruction = None
    fontInstruction = None
    endGame = None
    winner = None
    spriteWinner = None
    recWinner = None

    def __init__(self, lifepointJ1, lifepointJ2, goldJ1, goldJ2, manaJ1, manaJ2):
        self.font = pygame.font.SysFont("comicsansms", 72)
        self.fontInstruction = pygame.font.SysFont("comicsansms", 20)
        self.fontWinner = pygame.font.SysFont("comicsansms", 80)
        self.lifepointJ2 = lifepointJ2
        self.lifepointJ1 = lifepointJ1
        self.spriteJ1 = self.font.render(str(self.lifepointJ1), True, (0, 128, 0))
        self.spriteJ2 = self.font.render(str(self.lifepointJ2), True, (0, 128, 0))
        self.recJ1 = self.spriteJ1.get_rect(center=(200, 350))
        self.recJ2 = self.spriteJ2.get_rect(center=(800, 350))
        self.goldJ1 = goldJ1
        self.goldJ2 = goldJ2
        self.spriteGoldJ1 = self.font.render(str(self.goldJ1), True, (255, 255, 0))
        self.spriteGoldJ2 = self.font.render(str(self.goldJ2), True, (255, 255, 0))
        self.recGoldJ1 = self.spriteGoldJ1.get_rect(center=(300, 350))
        self.recGoldJ2 = self.spriteGoldJ2.get_rect(center=(900, 350))

        self.manaJ1 = manaJ1
        self.manaJ2 = manaJ2
        self.spriteManaJ1 = self.font.render(str(self.manaJ1), True, (0, 0, 255))
        self.spriteManaJ2 = self.font.render(str(self.manaJ2), True, (0, 0, 255))
        self.recManaJ1 = self.spriteManaJ1.get_rect(center=(400, 350))
        self.recManaJ2 = self.spriteManaJ2.get_rect(center=(1000, 350))

        self.spriteInstruction = self.fontInstruction.render('Appuyer sur la touche A pour terminer votre tour', True, (255, 255, 255))
        self.recIntruction = self.spriteManaJ1.get_rect(center=(50, 36))

        self.spriteWinner = self.fontWinner.render('Fin de partie', True, (255, 255, 255))
        self.recWinner = self.spriteWinner.get_rect(center=(600, 600))

    def resolveLifePointAfterAttack(self, lifePoint, player):
        if player == 'Player 1':
            self.lifepointJ1 = lifePoint
            if self.lifepointJ1 < 1:
                self.winner = 'Player 2'
        if player == 'Player 2':
            self.lifepointJ2 = lifePoint
            if self.lifepointJ2 < 1:
                self.winner = 'Player 1'
        self.updateLifePointSprite()

    def updateLifePointSprite(self):
        self.spriteJ1 = self.font.render(str(self.lifepointJ1), True, (0, 128, 0))
        self.spriteJ2 = self.font.render(str(self.lifepointJ2), True, (0, 128, 0))

    def exhaustMonsterCard(self, idCase, player):
        if player == 'Player 1':
            self.monstersJ1[idCase][2] = 1

        if player == 'Player 2':
            self.monstersJ2[idCase][2] = 1

    def setHand(self, handJ1, handJ2):
        self.handJ1 = handJ1
        self.handJ2 = handJ2

    def resetExhaust(self, player):
        if player == 'Player 1':
            for monster in self.monstersJ1:
                monster[2] = 0

        if player == 'Player 2':
            for monster in self.monstersJ2:
                monster[2] = 0

    def emptyCaseMonster(self, player, case):
        if player == 'Player 1':
            self.monstersJ1[case][0] = 0

        if player == 'Player 2':
            self.monstersJ2[case][0] = 0

    def emptyCaseHand(self, player, case):
        if player == 'Player 1':
            self.fieldHandJ1[case][0] = 0

        if player == 'Player 2':
            self.fieldHandJ2[case][0] = 0

    def emptyCaseAction(self, player, case):
        if player == 'Player 1':
            self.actionsJ1[case][0] = 0

        if player == 'Player 2':
            self.actionsJ2[case][0] = 0

    def checkField(self, player):
        if player == 'Player 1':
            monsters = self.monstersJ2

        if player == 'Player 2':
            monsters = self.monstersJ1

        for monster in monsters:
            if monster[0] == 1:
                return False

        return True

    def updateGold(self, player, ammount):
        if player == 'Player 1':
            self.goldJ1 = self.goldJ1 + ammount

        if player == 'Player 2':
            self.goldJ2 = self.goldJ2 + ammount

        self.updateGoldSprite()

    def updateMana(self, player, ammount):
        if player == 'Player 1':
            self.manaJ1 = self.manaJ1 + ammount

        if player == 'Player 2':
            self.manaJ2 = self.manaJ2 + ammount

        self.updateManaSprite()

    def updateGoldSprite(self):
        self.spriteGoldJ1 = self.font.render(str(self.goldJ1), True, (255, 255, 0))
        self.spriteGoldJ2 = self.font.render(str(self.goldJ2), True, (255, 255, 0))

    def updateManaSprite(self):
        self.spriteManaJ1 = self.font.render(str(self.manaJ1), True, (0, 0, 255))
        self.spriteManaJ2 = self.font.render(str(self.manaJ2), True, (0, 0, 255))
