def collision(event, field, fieldStatus, Player):
    fieldMonsterCard = None
    hand = None
    fieldActionCard = None
    if Player == 'Player 1':
        fieldMonsterCard = fieldStatus.__getattribute__('monstersJ1')
        fieldActionCard = fieldStatus.__getattribute__('actionsJ1')
        hand = fieldStatus.__getattribute__('handJ1')
        gold = fieldStatus.__getattribute__('goldJ1')
        mana = fieldStatus.__getattribute__('manaJ1')


    elif Player == 'Player 2':
        fieldMonsterCard = fieldStatus.__getattribute__('monstersJ2')
        fieldActionCard = fieldStatus.__getattribute__('actionsJ2')
        hand = fieldStatus.__getattribute__('handJ2')
        gold = fieldStatus.__getattribute__('goldJ2')
        mana = fieldStatus.__getattribute__('manaJ2')

    handCards = hand.__getattribute__('cards')
    position = event
    for card in field:
        if card.__getattribute__('position')[0] - 50 < position[0] < (card.__getattribute__('position')[0] + 50):
            if card.__getattribute__('position')[1] - 50 < position[1] < card.__getattribute__('position')[1] + 50:
                if card.__getattribute__('type') == 'Monster':
                    print('Action Monster card')
                if card.__getattribute__('type') == 'Action':
                    print('Activation Action card')

    for card in handCards:
        if card.__getattribute__('position')[0] - 50 < position[0] < (card.__getattribute__('position')[0] + 50):
            if card.__getattribute__('position')[1] - 50 < position[1] < card.__getattribute__('position')[1] + 50:
                if card.__getattribute__('type') == 'Monster':
                    case = 0
                    sacrifice = card.__getattribute__('stats')[1]
                    gold = gold - sacrifice
                    if gold >= 0:
                        fieldStatus.updateGold(Player, -sacrifice)
                        for monster in fieldMonsterCard:
                            if monster[0] == 0:
                                card.setRec(monster[1])
                                card.setPosition(monster[1])
                                fieldStatus.emptyCaseHand(Player, card.__getattribute__('case'))
                                card.setCase(case)
                                fieldStatus.exhaustMonsterCard(case, Player)
                                monster[0] = 1
                                hand.summon(card, field)
                                card.setField(True)
                                break
                            case += 1
                if card.__getattribute__('type') == 'Action':
                    case = 0
                    sacrifice = card.__getattribute__('stats')[1]
                    mana = mana - sacrifice
                    if mana >= 0:
                        fieldStatus.updateMana(Player, -sacrifice)
                        for action in fieldActionCard:
                            if action[0] == 0:
                                card.setRec(action[1])
                                card.setPosition(action[1])
                                fieldStatus.emptyCaseHand(Player, card.__getattribute__('case'))
                                card.setCase(case)
                                action[0] = 1
                                card.setField(True)
                                hand.summon(card, field)
                                break
                            case += 1


def detail(event, field, hand):
    handCards = hand.__getattribute__('cards')
    position = event
    for card in field:
        if card.__getattribute__('position')[0] - 50 < position[0] < (card.__getattribute__('position')[0] + 50):
            if card.__getattribute__('position')[1] - 50 < position[1] < card.__getattribute__('position')[1] + 50:
                return card
    for card in handCards:
        if card.__getattribute__('position')[0] - 50 < position[0] < (card.__getattribute__('position')[0] + 50):
            if card.__getattribute__('position')[1] - 50 < position[1] < card.__getattribute__('position')[1] + 50:
                return card


def directAttak(card, fieldStatus, player):
    stats = card.__getattribute__('stats')[0]
    case = card.__getattribute__('case')
    lifepointJ2 = fieldStatus.__getattribute__('lifepointJ2')
    lifepointJ1 = fieldStatus.__getattribute__('lifepointJ1')
    fieldMonsterJ1 = fieldStatus.__getattribute__('monstersJ1')
    fieldMonsterJ2 = fieldStatus.__getattribute__('monstersJ2')
    score = 0
    if player == 'Player 1' and fieldMonsterJ1[case][2] != 1:
        fieldStatus.exhaustMonsterCard(case, player)
        score = lifepointJ2 - stats
        print('le score J2', score)
        fieldStatus.resolveLifePointAfterAttack(score , 'Player 2')
    elif player == 'Player 2' and fieldMonsterJ2[case][2] != 1:
        print('here 2')
        score = lifepointJ1 - stats
        fieldStatus.exhaustMonsterCard(case, 'Player  1')
        fieldStatus.resolveLifePointAfterAttack(int(lifepointJ1) - stats, player)



def attakMonster(mineMonster, oponentMonster, graveyard, fieldCard, fieldStatus, currentPlayer):
    attakMine = mineMonster.__getattribute__('stats')[0]
    attakOponent = oponentMonster.__getattribute__('stats')[0]
    mineMonsterCase = mineMonster.__getattribute__('case')

    if currentPlayer == 'Player 1':
        oponent = 'Player 2'
        mineLifePoint = fieldStatus.__getattribute__('lifepointJ1')
        oponenLifePoint = fieldStatus.__getattribute__('lifepointJ2')
        monstersField = fieldStatus.__getattribute__('monstersJ1')
    elif currentPlayer == 'Player 2' :
        oponent = 'Player 1'
        mineLifePoint = fieldStatus.__getattribute__('lifepointJ2')
        oponenLifePoint = fieldStatus.__getattribute__('lifepointJ1')
        monstersField = fieldStatus.__getattribute__('monstersJ2')

    if monstersField[mineMonsterCase][2] != 1:
        score = attakMine - attakOponent
        print(' le score ', score)
        if score == 0:
            graveyard.append(oponentMonster)
            graveyard.append(mineMonster)
        elif score > 0:
            graveyard.append(oponentMonster)
            fieldStatus.resolveLifePointAfterAttack(int(oponenLifePoint) - score, oponent)
        else:
            graveyard.append(mineMonster)
            fieldStatus.resolveLifePointAfterAttack(int(mineLifePoint) + score, currentPlayer)
        for dMonsters in graveyard:
            for card in fieldCard:
                if dMonsters == card:
                    owner = card.__getattribute__('owner')
                    case = card.__getattribute__('case')
                    fieldStatus.emptyCaseMonster(owner, case)
                    fieldCard.remove(card)


def manageGold(fielCards, fieldStatus, currentPlayer):
    for card in fielCards:
        if card.__getattribute__('type') == 'Monster':
            owner = card.__getattribute__('owner')
            if owner == currentPlayer:
                goldMonster = card.__getattribute__('stats')[1]
                fieldStatus.updateGold(owner, goldMonster)


def manageEffect(fieldCards, fieldStatus, currentPlayer, card, graveyard):
    name = card.__getattribute__('name')
    if name == 'Gobelin parvenu':
        fieldStatus.updateGold(currentPlayer, 5)
        graveyard.append(card)

    for dMonsters in graveyard:
        for card in fieldCards:
            if dMonsters == card:
                owner = card.__getattribute__('owner')
                case = card.__getattribute__('case')
                if owner == 'Player 1':
                    fieldStatus.emptyCaseAction(owner, case)
                fieldCards.remove(card)
