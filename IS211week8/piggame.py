import datetime
import random



def throw_the_die(sides=6):
    """
    Simulate throwing a die
    :param sides: number of sides
    :return: Values
    """
    return random.randint(1, sides)

class Player:

    def __init__(self, name):
        self.name = name
        self.total = 0

    def __str__(self):
        return f"{self.name}'s Total = {self.total}"

    def show(self):
        print(f"{self}")

    def turn(self):
        pass

class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.dice = throw_the_die()

    
    def turn(self):
        self.total = 0

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)



    def turn(self):
        """
        Play one turn
        :return:
        """
        turn_total = 0
        roll_hold = None
        while roll_hold != "h":

            roll_hold = input("Roll(r) or Hold(h)? ").lower()
            if roll_hold == "h":
                continue
            die = throw_the_die()
            self.total += die
            print(f"{self.name}")
            print(f'{self.name} You rolled a:', die)
            print(f'{self.name} Total points', self.total)
            print(f'{self.name} Score if hold:', self.total + turn_total)


            if die != 1:
                print(f'{self.name} Your score for this round is {self.total}')

            else:
                print(f'{self.name} pigged it')
                self.total = 0
                break
        

        self.show()




class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.winner = None
        self.current_player = self.players[0]

    
    
      

    def check_winner(self):
        """
        Returns true if there is winner
        :return:
        """
        

        for player in self.players:
            if player.total >= 100:
                self.winner = player
                return True
                
        return False

    def play_game(self):
    
        while not self.check_winner():
            self.current_player.turn()
            self.check_winner()
            self.change_player()

        print(f"Winner! {self.winner}")

    
    def change_player(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]


class TimedGame(Game):

    def __init__(self, player1, player2, time_limit):
        super().__init__(player1, player2)
        self.start_time = datetime.datetime.now()
        self.time_limit = time_limit

    def check_time(self, time_now):
        if (time_now - self.start_time).total_seconds() > self.time_limit:
            return print("Time expired")
        
   
    def play_game(self):
        current_player = self.players[0]
        time_flag = False 

        while not self.check_winner or not time_flag:
            self.play_game()
            self.current_player
            self.change_player()
            current_player = (current_player + 1)

            
            time_flag = self.check_time(datetime.datetime.now())
        
        self.check_time()
        self.check_winner()



def make_player(player_type, player_name):

    if player_type.upper() == 'C':
        return HumanPlayer(player_name)
    elif player_type.upper() == 'H':
        return  HumanPlayer(player_name)
    else:
        raise ValueError("I don't know ")





def main():
    p1 = HumanPlayer("Orlando")
    p2 = HumanPlayer("Steph")
    pig_game = Game(p1, p2)
    pig_game.play_game()


if __name__ == "__main__":
    main()

