import random
class Board:
    def __init__(self, size,n,m):
        self.size = size
        #snake and ladder configurations
        self.snakes = {}
        self.ladders = {}
        #user input for the snake and ladder configurations
        for i in range(n):
            snake_head = int(input("Enter snakes's head: "))
            snake_tail = int(input("Enter snakes's tail: "))
            self.snakes[snake_head] = snake_tail
        print(self.snakes)
        for i in range(m):
            ladder_bottom = int(input("Enter ladder's bottom: "))
            ladder_top = int(input("Enter ladder's top: "))
            self.ladders[ladder_bottom] = ladder_top
        print(self.ladders)
    #checks for snake bite and ladder climb
    def check_snake_or_ladder(self, position):
        if position in self.snakes:
            print("Oops!!sanke Bite", self.snakes[position])
            return self.snakes[position]
        elif position in self.ladders:
            print("hurray!!Ladder Climb", self.ladders[position])
            return self.ladders[position]
        else:
            return position
class Dice:
    def __init__(self, sides):
        self.sides = sides
    def roll(self):
        return random.randint(1, self.sides)
class Gameplayer:
    def __init__(self, name):
        self.name = name
        #player starts from position 1
        self.position = 1
class Game:
    def __init__(self, board, dice, players):
        self.board = board
        self.dice = dice
        self.players = players
        self.current_player = None
        self.winner = None
    def play(self):
        print("Starting game!")
        while not self.winner:
            for player in self.players:
                self.current_player = player
                print("\nIt's", player.name, "'s turn!")
                A=input("enter \"A\" to roll dice")
                self.play_turn()
                if self.current_player.position == self.board.size:
                    self.winner = player
                    break
        print("\nCongratulations,", self.winner.name, "! You won the game!")
    def play_turn(self):
        #rolling dice
        roll = self.dice.roll()
        print("You rolled a", roll)
        new_position = self.current_player.position + roll
        #if the value is greater than size then previous position will hold
        if new_position > self.board.size:
            print("Oops, you can't move past the end of the board. Try again next turn!")
            return
        print("Moving from", self.current_player.position, "to", new_position)
        self.current_player.position = self.board.check_snake_or_ladder(new_position)
        print("You are now at position", self.current_player.position)
# create board
board = Board(100,7,8)
# create dice
dice = Dice(6)
# create players
player1 = Gameplayer("player 1")
player2 = Gameplayer("player 2")
# create game
game = Game(board, dice, [player1, player2])
# start game
game.play()