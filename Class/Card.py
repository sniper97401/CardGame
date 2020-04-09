import pygame


class Card:
    name = None
    type = None
    description = None
    sprite = None
    path = None
    position = None
    rec = None
    stats = None
    case = None
    owner = None
    field = None

    listCard = [
        ['Dragon Blanc aux yeux bleus', 'Monster', 'Puisssant Dragon', 'dragonBlanc.jpg', (30, 8), False],
        ['Magicien des ténèbres', 'Monster', 'Puisssant Magicien', 'DarkMagician.jpg', (25, 7), False],
        ['Gobelin parvenu', 'Action', 'Vous récupérez 5 pièces d\'ors ', 'gobelin-parvenu.jpg', (0, 7), False]
    ]

    def __init__(self, name):
        self.name = name
        for card in self.listCard:
            if card[0] == name:
                self.type = card[1]
                self.description = card[2]
                self.path = card[3]
                self.sprite = pygame.transform.scale(pygame.image.load(self.path).convert_alpha(), ((67, 58)))
                self.stats = card[4]
                self.field = card[5]


    def setPosition(self, pos):
        self.position = pos

    def setRec(self, rec):
        self.rec = self.sprite.get_rect(center=rec)

    def setCase(self, case):
        self.case = case

    def setOwner(self, player):
        self.owner = player

    def setField(self, status):
        self.field = status


