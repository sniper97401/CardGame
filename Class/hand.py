class Hand:
    cards = None

    def __init__(self):
        self.cards = []

    def drawCard(self, cards, field, Player):
        if Player == 'Player 1':
            caseHand = field.__getattribute__('fieldHandJ1')
        elif Player == 'Player 2':
            caseHand = field.__getattribute__('fieldHandJ2')

        for card in cards:
            cpt = 0
            for case in caseHand:
                if case[0] != 1:
                    card.setCase(cpt)
                    card.setPosition(case[1])
                    card.setRec(case[1])
                    card.setOwner(Player)
                    case[0] = 1
                    self.cards.append(card)
                    break


    def summon(self, selectedCard, field):
        for card in self.cards:
            if card == selectedCard:
                field.append(card)
                self.cards.remove(card)
