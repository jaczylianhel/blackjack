import random


class Docker:
    Dock = []


suits_symbols = ['♠', '♦', '♥', '♣']
for color in suits_symbols:
    for num in range(2, 15):
        if num < 11:
            Docker.Dock.append(color + str(num))
        elif num == 11:
            Docker.Dock.append(color + 'J')
        elif num == 12:
            Docker.Dock.append(color + 'Q')
        elif num == 13:
            Docker.Dock.append(color + 'K')
        else:
            Docker.Dock.append(color + 'A')


class Player(Docker):
    # boolChoice = True
    playerHand = []
    playerSum = 0
    betCash = 0
    nCard = 3

    def __init__(self, account):
        self.account = account

    def firstCardsPlayer(self, playerHand):
        for card in range(0, 2):
            self.playerHand.append(Player.Dock[card * 2])
        return playerHand

    def printCardsPlayer(self, playerHand):
        for card in range(0, len(self.playerHand)):
            print(f'PlayOne---> {card+1} in Hand is: {self.playerHand[card]}')

    def inputAccount(self):
        while True:
            try:
                account = int(input('How much do you have $'))
            except ValueError:
                print('Wrong!!Enter the number')
                continue
            else:
                self.account = account
                break
        return account

    def stillBet(self):
        while True:
            try:
                betCash = int(input('How much bet $'))
                if (betCash > self.account):
                    print(f"You don't have enough money. Your bank is: ${self.account}")
                    continue
            except ValueError:
                print('Wrong!!Enter the number')
                continue
            else:
                self.account -= betCash
                print('\nThank You!\n')
                break
        return betCash, self.account

    def decision(self, answer):
        if (answer == 1):
            return True
        elif (answer == 2):
            return False
        else:
            print('soon...')

    def playerTurn(self, playerHand, playerSum):
        PlayOne.playerHit(PlayOne.playerHand)  # Player draw card
        PlayOne.printCardsPlayer(PlayOne.playerHand)  # Player print all card on hand
        PlayOne.playerSum = PlayOne.checkSum(PlayOne.playerHand)  # Player sum card
        print(f'\nPlayOne ---> Sum card is: {PlayOne.playerSum}')  # show  Player sum card
        if PlayOne.checkPlayerLose():
            return True

    def playerHit(self, playerHand):
        betAgain, self.account = self.stillBet()
        self.betCash += betAgain
        print('pobrano karte')
        Player.nCard += 1
        return self.playerHand.append(Player.Dock[self.nCard])

    def checkSum(self, playerHand, playerSum=0):
        for card in self.playerHand:
            if card[1] == 'K' or card[1] == 'Q' or card[1] == 'J' or card[1:] == '10':
                playerSum += 10
            elif card[1] == 'A':
                playerSum += 11
            else:
                playerSum += int(card[1])
        return playerSum

    def checkPlayerLose(self):
        if self.playerSum > 21:
            print(f"\nYou loose: ${self.betCash}")
            print(f"Your actually account is : ${self.account}")
            return True

    def checkPlayerBlackjack(self):

        if self.playerSum == 21:
            print('BlackJack!!!')
            self.account += (self.betCash * 2)
            print(f"Your actually account is: ${self.account}")
            return True

    def playerChooseTurn(boolChoice=True):
        while boolChoice:
            try:
                choice = int(input('\nDo you wanna still game? 1-Hit, 2-Stand, 3-DoubleDown '))
                if choice in [1, 2, 3]:
                    print(f'\nYou choose: {choice}\n')
                    break
                else:
                    print('Wrong choice!! Try again')
                    continue
            except:
                print("Wrong! Please insert number 1-3")
        return choice


class Computer(Docker):
    computerHand = []
    computerSum = 0
    card = 3

    def firstCardsComputer(self, computerHand):
        for card in range(0, 2):
            self.computerHand.append(Computer.Dock[(card * 2) + 1])

    def checkSum(self, computerHand, computerSum=0):
        for card in self.computerHand:
            if card[1] == 'K' or card[1] == 'Q' or card[1] == 'J' or card[1:] == '10':
                computerSum += 10
            elif card[1] == 'A':
                computerSum += 11
            else:
                computerSum += int(card[1])
        return computerSum

    def computerTurn(self, computerHand):
        for card in range(0, len(self.computerHand)):
            print(f'Computer---> {card+1} in Hand is: {self.computerHand[card]}')

        while True:
            self.computerSum = self.checkSum(self.computerHand)
            print(f'Computer ---> Sum card is: {self.computerSum}')

            if self.computerSum <= 16:
                Player.nCard += 1
                self.computerHand.append(Computer.Dock[Player.nCard])
                print(f'Computer---> {self.card} in Hand is: {Com1.computerHand[self.card-1]}')
                Computer.card += 1
            elif self.computerSum == 21:
                print('BlackJack!!! You Loose')
                break
            else:
                break
        return self.computerSum


#################################################################################
# Enter the player name
PlayOne = Player(0)
Com1 = Computer()
BlackJack = True
game = True
random.shuffle(Docker.Dock)
# Set your Account
PlayOne.account = PlayOne.inputAccount()

# Set your bet
PlayOne.betCash, PlayOne.account = PlayOne.stillBet()
# print(f'Bet:{PlayOne.betCash}, Left: {PlayOne.account}\n')
while BlackJack:
    while game:
        # Give a card on table
        PlayOne.firstCardsPlayer(PlayOne.playerHand)
        Com1.firstCardsComputer(Com1.computerHand)

    # print Player cards and sum
        PlayOne.printCardsPlayer(PlayOne.playerHand)  # Player print card on table
        PlayOne.playerSum = PlayOne.checkSum(PlayOne.playerHand)  # Player sum card
        print(f'PlayOne ---> Sum card is: {PlayOne.playerSum}')  # show  Player sum card
    # print Computer hand (first card)
        # Computer print first card
        print(f'\nComputer ---> 1 in Hand is: {Com1.computerHand[0]}\n')

    # Game after first round
        while True:
            # Check condition
            if PlayOne.checkPlayerLose():
                game = False
                break
            if PlayOne.checkPlayerBlackjack():
                game = False
                break
            print(f"Your account: ${PlayOne.account}")

            if (PlayOne.decision(PlayOne.playerChooseTurn())) == False:  # Player enter the '2'  Stand
                Com1.computerTurn(Com1.computerHand)
                break
            else:  # Player enter the '1' hit
                if PlayOne.playerTurn(PlayOne.playerHand, PlayOne.playerSum):  # if player lose?
                    game = False
                    break
        if game == False:
            break
    # case in no BlackJack and sum cards Player and Computers <21
        PlayOne.playerSum = PlayOne.checkSum(PlayOne.playerHand)  # Player sum card
        Com1.computerSum = Com1.checkSum(Com1.computerHand)  # Computer sum card

    # Who win?

        if PlayOne.playerSum > Com1.computerSum or Com1.computerSum > 21:
            PlayOne.account = PlayOne.account + (PlayOne.betCash * 2)
            print(
                f'You Win!!!\nYour sum is {PlayOne.playerSum}\nComputer sum is {Com1.computerSum}\n')
            print(f"Your account: ${PlayOne.account}")
            break
        elif PlayOne.playerSum == Com1.computerSum:
            print(
                f'!!Draw!!\nYour sum is {PlayOne.playerSum}\nComputer sum is {Com1.computerSum}\n')
            print(f"Your account: ${PlayOne.account}")
            break
        else:
            print(
                f'You Lose :(\nYour sum is {PlayOne.playerSum}\nComputer sum is {Com1.computerSum}\n')
            print(f"Your account: ${PlayOne.account}")
            break

    again = input('Wanna Again (y/n): ')
    if again.lower() == 'y':
        game = True
        random.shuffle(Docker.Dock)
        PlayOne.playerHand = []
        PlayOne.playerSum = 0
        PlayOne.betCash = 0
        PlayOne.nCard = 3
        Com1.computerHand = []
        Com1.computerSum = 0
        Com1.card = 3
    else:
        break
