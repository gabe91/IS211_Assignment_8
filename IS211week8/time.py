import random
import sys
import time
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turnscore = 0

    def decide(self):
        while True:
            decision = input("Would you like to roll or hold? (r/h) ")
            if(decision == "r"):
                return 1
            elif(decision == "h"):
                return 0
            else:
                print("Please enter a valid input!")

    def roll(self, diceRoll):
        if(diceRoll == 1):
            print("You rolled a 1, your turn is over, and you got 0 points for this round!")
            self.score -= self.turnscore
            self.turnscore = 0
            return 0
        else:
            print("You rolled a " + str(diceRoll) + ", your turn continues!")
            self.score += diceRoll
            self.turnscore += diceRoll
        
    def hold(self):
        print("You have chosen to hold, your turn is over, and you got " + str(self.turnscore) + " points for this round!")
        self.turnscore = 0

    def __str__(self):
        return self.name + " Score: " + str(self.score)

class ComputerPlayer(Player):

    def decide(self):
        time.sleep(0.1)
        threshold = min(25, 100 - (self.score - self.turnscore))
        if(self.turnscore >= threshold):
            return 0 # hold
        else:
            return 1 # roll dice

    def roll(self, diceRoll):
        if(diceRoll == 1):
            print(self.name + " rolled a 1, their turn is over, and they got 0 points for this round!")
            self.score -= self.turnscore
            self.turnscore = 0
            return 0
        else:
            print(self.name + " rolled a " + str(diceRoll) + ", their turn continues!")
            self.score += diceRoll
            self.turnscore += diceRoll
            
    def hold(self):
        print(self.name + " have chosen to hold, their turn is over, and they got " + str(self.turnscore) + " points for this round!")
        self.turnscore = 0

class PlayerFactory:
    computercount = 0
    humancount = 0
    def createPlayer(type):
        if(type == "computer"):
            PlayerFactory.computercount += 1
            return ComputerPlayer("Computer " + str(PlayerFactory.computercount))
        elif(type == "human"):
            # get name from user
            PlayerFactory.humancount += 1
            name = input("Please enter Player " + str(PlayerFactory.humancount) + "'s name: ")
            return Player(name)
        else:
            raise Exception("Invalid player type")

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = 1

    def doStep(self):
        if(self.turn == 1):
            print("\nIt is " + self.player1.name + "'s turn")
            decision = self.player1.decide()
            if(decision == 1):
                diceRoll = random.randint(1,6)
                self.player1.roll(diceRoll)
                if diceRoll == 1:
                    self.turn = 2
            else:
                self.player1.hold()
                self.turn = 2
            print(self.player1)
            print(self.player2)
        else:
            print("\nIt is " + self.player2.name + "'s turn")
            decision = self.player2.decide()
            if(decision == 1):
                diceRoll = random.randint(1,6)
                self.player2.roll(diceRoll)
                if diceRoll == 1:
                    self.turn = 1
            else:
                self.player2.hold()
                self.turn = 1
            print(self.player1)
            print(self.player2)

        
        if(self.player1.score >= 100):
            print(self.player1.name + " wins!")
            exit()
        elif(self.player2.score >= 100):
            print(self.player2.name + " wins!")
            exit()

class TimedGameProxy:
    def __init__(self, player1, player2):
        self.game = Game(player1, player2)
        self.startime = time.time()
        self.maxtime = 60
    
    def doStep(self):
        if(time.time() - self.startime > self.maxtime):
            print("Game has timed out!")
            exit()
        self.game.doStep()
            
def main():
    timed = False
    for i in range(len(sys.argv)):
        if(sys.argv[i] == "--player1"):
            player1Type = sys.argv[i+1]
        if(sys.argv[i] == "--player2"):
            player2Type = sys.argv[i+1]
        if(sys.argv[i]) == "--timed":
            timed = True

    player1 = PlayerFactory.createPlayer(player1Type)
    player2 = PlayerFactory.createPlayer(player2Type)


    if(timed):
        game = TimedGameProxy(player1, player2)
    else:
        game = Game(player1, player2)
    while(True):
        game.doStep()

if __name__ == "__main__":
    main()
    