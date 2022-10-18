import argparse
from datetime import datetime
import random
import sys


def throw_the_die(sides=6):


    return random.randint(1, sides)



class Computer:
    def __init__(self, name):
        self.name = name 
        self.total = 0
        self.comp_total = 0
        #scratch = False

    def __str__(self):
        return f"{self.name}"

    def round(self):
        if self.total < 20:
           die = throw_the_die()
           print(f"Computer rolls {die}")
           if die != 1:
                self.total += die
                print(f"Round score is {self.total}")
                self.round()
                self.total = 0
           else:
                print("You pigged it")
                self.total = 0
                self.comp_total += self.total
                print(f"Computer total is {self.comp_total}")
        else:
            print("Computer holds")
            self.comp_total += self.total
            (f"Computer total {self.comp_total}")
            self.total = 0
    
    """def turn_total(self):
        scratch = False

        while self.comp_total >= min(self.total, 100 - self.turn_total):
            die = throw_the_die()

            if die == 1:
                self.total = 0
                print("You pigged it")
                scratch = True
                break

            self.comp_total += die
            print("Recommendations is to: ")
            print(f"{self.comp_total}")
            print(f"Possible total if hold, {self.turn_total + self.total}")
            print(f"{self.comp_total}")
    

        if not scratch:
            self.turn_total += self.total
            print(f"Your total score is {self.turn_total}")
            self.turn_total = 0

        self.turn.total()"""

        
class Player:

    def __init__(self, name):
        self.name = name
        self.total = 0
        self.turn_total = 0


    #def show(self):
    #    return(f"{self}")

    def __str__(self):
        return f"{self.name}'s total = {self.total}"

    def turn(self):

        roll_hold = 'r'
        
        while roll_hold != "h":
            #die = throw_the_die()

            roll_hold = input("Roll(r) or Hold(h)? ").lower()
            if roll_hold == 'h':
                break 
            die = throw_the_die()
            print(f'rolled {die}')

            if die != 1:
                self.total += die
                print(f'Your score for this round is {self.total}')
            else:
                print('You pigged it!')
                self.total = 0
                break
        self.turn_total += self.total
        print(f"Your total score is {self.turn_total}")
        self.turn_total = 0


            

      


        
            

        #self.show()


"""class ComputerPlayer(Player):
    
    def __init__(self, name):
        super().__init__(name)

    def turn(self):

        turn_total = 0
        scratch = False
        

        while turn_total >= min(self.total, 100 - self.turn_total):
            die = throw_the_die()
            roll_hold = input("Roll(r) or Hold(h)").lower()
            if die == 1:
                self.total = 0
                print("You pigged it")
                scratch = True
                break

            turn_total += die
            print("Recommendations is to: ")
            print(f"{turn_total}")
            print(f"Possible total if hold, {self.turn_total + self.total}")
            print(f"{turn_total}")
            return roll_hold

        if not scratch:
            self.turn_total += self.total
            print(f"Your total score is {self.turn_total}")
            self.turn_total = 0 """
        
        



class Game:
    def __init__(self):
        #self.player2 = Player2("player 2")
        self.player = Player("Player")
        self.computer = Computer("Computer")
        self.winner = None

    def choose_player(self):
        rng = random.randint(1, 10)
        if rng < 6:
            print("Computer goes first")
            while self.computer.total < 100 and self.player.total < 100:
                self.computer.round()
                self.player.turn()

                if self.computer.total >= 100:
                    print("Computer wins")
                    return
                else:
                    print("Player wins")
                
        else:
            print("Player goes first")
            while self.computer.total < 100 and self.player.total < 100:
                self.player.turn()
                self.computer.round()
                if self.computer.total >= 100:
                    print("Computer wins")
                else:
                    print("Player wins")
                    return


        self.choose_player()


class TimedGame(Game):

    def __init__(self, time_limit):
        self.start_time = datetime.time()
        self.time_limit = time_limit
        Game.__init__(self, Player='Player', Computer='Computer')

    def check_time(self, time_now):
        return (time_now - self.start_time) > self.time_limit

    
    def play_game(self):

        time_flag = False

        while not self.choose_player() or not time_flag:
            self.choose_player()

            time_flag = self.check_time(datetime.time())
    
        self.check_time()
        self.choose_player()


    def make_player(player_type, player_name):

        if player_type.upper() == 'C':
            return Computer(player_name)
        elif player_type.upper() == 'H':
            return Player(player_name)
        else:
            raise ValueError("I don't know!")



def main():
    game = Game()
    game.choose_player()

if __name__ == '__main__':
   main()