import pygame


class DescriptionCard:
    spriteTitle = None
    rectTitle = None
    spriteDescription = None
    rectDescription = None
    spriteImage = None
    rectImage = None
    spriteAttack = None
    rectAttack = None
    spriteGold = None
    rectGold = None

    def __init__(self, card, player):
        if card:
            fontDescription = pygame.font.SysFont("black", 36)
            fontAttak = pygame.font.SysFont("black", 30)
            attack = card.__getattribute__('stats')[0]
            gold = card.__getattribute__('stats')[1]
            self.spriteTitle = fontDescription.render(card.__getattribute__('name'), True, (255, 255, 255))
            self.rectTitle = self.spriteTitle.get_rect(center=(600, 410))

            self.spriteDescription = fontDescription.render(card.__getattribute__('description'), True, (255, 255, 255))
            self.rectDescription = self.spriteDescription.get_rect(center=(600, 660))

            self.spriteImage = pygame.transform.scale(pygame.image.load(card.__getattribute__('path')).convert_alpha(), ((200, 200)))
            self.rectImage = self.spriteImage.get_rect(center=(600, 540))

            if card.__getattribute__('type') == 'Monster' and card.__getattribute__('owner') == player:
                self.spriteAttack = fontAttak.render('Attack : ' + str(attack), True, (255, 0, 0))
                self.rectAttack = self.spriteAttack.get_rect(center=(420, 540))
                self.spriteGold = fontAttak.render('Gold : ' + str(gold), True, (255, 255, 0))
                self.rectGold = self.spriteGold.get_rect(center=(770, 540))
            elif card.__getattribute__('type') == 'Monster' and card.__getattribute__('owner') != player and card.__getattribute__('field') == True:
                self.spriteAttack = fontAttak.render('Attack : ' + str(attack), True, (255, 0, 0))
                self.rectAttack = self.spriteAttack.get_rect(center=(420, 540))
                self.spriteGold = fontAttak.render('Gold : ' + str(gold), True, (255, 255, 0))
                self.rectGold = self.spriteGold.get_rect(center=(770, 540))

            if card.__getattribute__('type') == 'Action' and card.__getattribute__('owner') == player:
                self.spriteAttack = fontAttak.render('', True, (255, 0, 0))
                self.rectAttack = self.spriteAttack.get_rect(center=(420, 540))
                self.spriteGold = fontAttak.render('Mana : ' + str(gold), True, (0, 0, 255))
                self.rectGold = self.spriteGold.get_rect(center=(770, 540))
            elif card.__getattribute__('type') == 'Action' and card.__getattribute__('owner') != player and card.__getattribute__('field') == True:
                self.spriteAttack = fontAttak.render('', True, (255, 0, 0))
                self.rectAttack = self.spriteAttack.get_rect(center=(420, 540))
                self.spriteGold = fontAttak.render('Mana : ' + str(gold), True, (0, 0, 255))
                self.rectGold = self.spriteGold.get_rect(center=(770, 540))


