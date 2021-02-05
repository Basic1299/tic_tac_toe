import random


class Player():
    def __init__(self, image, name):
        self.image = image
        self.name = name
        self.win = False

    def option(self):
        while True:
            option = input(f"{self.name}({self.image}) plays: ")
            if len(option) == 2 and option != " " and (option in "1a 2a 3a 1b 2b 3b 1c 2c 3c" or option in "a1 a2 a3 b1 b2 b3 c1 c2 c3"):
                return option
            else:
                print("Invalid Input! Try again.")


class Computer():
    def __init__(self, image, name):
        self.image = image
        self.name = name
        self.win = False
        self.path = []
        self.path_index = 0

    def cpu_play(self, board):
        if len(self.path) == 0:
            self.find_path(board)
        elif len(self.path) == 3:
            self.confirm_path(board)
        elif len(self.path) == 1:
            self.random_spot(board)


        return self.path[self.path_index]

    def confirm_path(self, board):
        if board[self.path[0][0]][self.path[0][1]] == "x" or board[self.path[1][0]][self.path[1][1]] == "x" or board[self.path[2][0]][self.path[2][1]] == "x":
            self.find_path(board)
            self.set_path_index(board)
            
        elif board[self.path[0][0]][self.path[0][1]] == "o" or board[self.path[1][0]][self.path[1][1]] == "o" or board[self.path[2][0]][self.path[2][1]] == "o":
            self.set_path_index(board)

        else:
            if self.path_index < 2:
                self.path_index += 1

    def set_path_index(self, board):
        if board[self.path[0][0]][self.path[0][1]] == "o" and board[self.path[1][0]][self.path[1][1]] == "o":
            self.path_index = 2
        elif board[self.path[0][0]][self.path[0][1]] == "o":
            self.path_index = 1
        else:
            self.path_index = 0

    def find_path(self, board):
        num = random.randint(0, 2)
        
        # Randomly find patterns
        if num == 0:
            self.rows(board)
            if len(self.path) == 0:
                self.columns(board)
                if len(self.path) == 0:
                    self.crosses(board)
        elif num == 1:
            self.columns(board)
            if len(self.path) == 0:
                self.rows(board)
                if len(self.path) == 0:
                    self.crosses(board)
        elif num == 2:
            self.crosses(board)
            if len(self.path) == 0:
                self.columns(board)
                if len(self.path) == 0:
                    self.rows(board)

        if len(self.path) == 0:
            self.random_spot(board)

    def random_spot(self, board):
        self.path_index = 0
        self.path.clear()
        
        coors = [random.randint(0, 2), random.randint(0, 2)]
        while True:
            if board[coors[0]][coors[1]] == "x" or board[coors[0]][coors[1]] == "o":
                coors = [random.randint(0, 2), random.randint(0, 2)]
            else:
                self.path.append(coors)
                break
               
    def crosses(self, board):
        """Returns cross possible way"""
        if board[0][0] != "x" and board[1][1] != "x" and board[2][2] != "x":
            self.path.clear()
            self.path_index = 0
            self.path.append([0, 0])
            self.path.append([1, 1])
            self.path.append([2, 2])
        
        elif board[2][0] != "x" and board[1][1] != "x" and board[0][2] != "x":
            self.path.clear()
            self.path_index = 0
            self.path.append([2, 0])
            self.path.append([1, 1])
            self.path.append([0, 2])

        else:
            self.path.clear()

    def columns(self, board):
        """Returns column possible way"""
        if board[0][0] != "x" and board[1][0] != "x" and board[2][0] != "x":
            self.path.clear()
            self.path_index = 0
            for i in range(3):
                self.path.append([i, 0])
        
        elif board[0][1] != "x" and board[1][1] != "x" and board[2][1] != "x":
            self.path.clear()
            self.path_index = 0
            for i in range(3):
                self.path.append([i, 1])
        
        elif board[0][2] != "x" and board[1][2] != "x" and board[2][2] != "x":
            self.path.clear()
            self.path_index = 0
            for i in range(3):
                self.path.append([i, 2])
        
        else:
            self.path.clear()

    def rows(self, board):
        """Returns row possible way"""
        if board[0][0] != "x" and board[0][1] != "x" and board[0][2] != "x":
            self.path.clear()
            self.path_index = 0
            for i in range(3):
                self.path.append([0, i])
        
        elif board[1][0] != "x" and board[1][1] != "x" and board[1][2] != "x":
            self.path.clear()
            self.path_index = 0
            for i in range(3):
                self.path.append([1, i])

        elif board[2][0] != "x" and board[2][1] != "x" and board[2][2] != "x":
            self.path.clear()
            self.path_index = 0
            for i in range(3):
                self.path.append([2, i])

        else:
            self.path.clear()


    

def print_board(board):
    print()
    print("   1 2 3")
    print("  #######")
    print(f"a #{board[0][0]}#{board[0][1]}#{board[0][2]}#")
    print("  #######")
    print(f"b #{board[1][0]}#{board[1][1]}#{board[1][2]}#")
    print("  #######")
    print(f"c #{board[2][0]}#{board[2][1]}#{board[2][2]}#")
    print("  #######")
    print()

def board_update_cpu(board, cpu_play, cpu):
    if cpu_play == [0, 0]:
        board[0][0] = cpu.image
    elif cpu_play == [0, 1]:
        board[0][1] = cpu.image
    elif cpu_play == [0, 2]:
        board[0][2] = cpu.image
    elif cpu_play == [1, 0]:
        board[1][0] = cpu.image
    elif cpu_play == [1, 1]:
        board[1][1] = cpu.image
    elif cpu_play == [1, 2]:
        board[1][2] = cpu.image
    elif cpu_play == [2, 0]:
        board[2][0] = cpu.image
    elif cpu_play == [2, 1]:
        board[2][1] = cpu.image
    elif cpu_play == [2, 2]:
        board[2][2] = cpu.image
        
    return board

def board_update(board, option, player):
    while True:
        if (option == "1a" or option == "a1") and board[0][0] == " ":
            board[0][0] = player.image
            return board, True
        elif (option == "2a" or option == "a2") and board[0][1] == " ":
            board[0][1] = player.image
            return board, True
        elif (option == "3a" or option == "a3") and board[0][2] == " ":
            board[0][2] = player.image
            return board, True
        elif (option == "1b" or option == "b1") and board[1][0] == " ":
            board[1][0] = player.image
            return board, True
        elif (option == "2b" or option == "b2") and board[1][1] == " ":
            board[1][1] = player.image
            return board, True
        elif (option == "3b" or option == "b3") and board[1][2] == " ":
            board[1][2] = player.image
            return board, True
        elif (option == "1c" or option == "c1") and board[2][0] == " ":
            board[2][0] = player.image
            return board, True
        elif (option == "2c" or option == "c2") and board[2][1] == " ":
            board[2][1] = player.image
            return board, True
        elif (option == "3c" or option == "c3") and board[2][2] == " ":
            board[2][2] = player.image
            return board, True
        else:
            print("The place is taken! Try again.")
            option = player.option()

def win_check(board, player):
    running = True
    
    # Rows
        # 1
    if board[0][0] == player.image and board[0][1] == player.image and board[0][2] == player.image:
        player.win = True
        running = False
        # 2
    elif board[1][0] == player.image and board[1][1] == player.image and board[1][2] == player.image:
        player.win = True
        running = False
        # 3
    elif board[2][0] == player.image and board[2][1] == player.image and board[2][2] == player.image:
        player.win = True
        running = False
    # Columns
        # 1
    elif board[0][0] == player.image and board[1][0] == player.image and board[2][0] == player.image:
        player.win = True
        running = False
        # 2
    elif board[0][1] == player.image and board[1][1] == player.image and board[2][1] == player.image:
        player.win = True
        running = False
        # 3
    elif board[0][2] == player.image and board[1][2] == player.image and board[2][2] == player.image:
        player.win = True
        running = False
    # crosses
        # top-left, middle, bottom-right
    elif board[0][0] == player.image and board[1][1] == player.image and board[2][2] == player.image:
        player.win = True
        running = False
        # bottom-left, middle, top-right
    elif board[2][0] == player.image and board[1][1] == player.image and board[0][2] == player.image:
        player.win = True
        running = False
    else:
        player.win = False

    return player.win, running

def not_full_board_check(board):
    """Checks if the board is not full"""
    for row in board:
        for unit in row:
            if unit == " ":
                return True
    return False

def name_input(player):
    while True:
        name = input(f"{player} enter your name: ")
        if len(name) > 0:
            break
        else:
            print("Invalid name! Try again.")
            
    return name

def player_vs_player(board):
    running = True

    # Players
    p1 = Player("x", name_input("Player 1"))
    p2 = Player("o", name_input("Player 2"))
    
    while running:
        if not p1.win or not p2.win:
            print_board(board)
            board = board_update(board, p1.option(), p1)
            p1.win, running = win_check(board, p1)
            if running:
                running = not_full_board_check(board)
 
            
            if not p1.win and running:
                print_board(board)
                board = board_update(board, p2.option(), p2)
                p2.win, running = win_check(board, p2)
                if running:
                    running = not_full_board_check(board)

    print_board(board)

    if p1.win or p2.win:
        if p1.win:
            print(f"{p1.name} won!")
        else:
            print(f"{p2.name} won!")
    else:
        print("Nobody won!")


def player_vs_computer(board):
    running = True

    p1 = Player("x", name_input("Player"))
    computer = Computer("o", "Computer")

    while running:
        if (not p1.win or not computer.win) and running:
            board = board_update_cpu(board, computer.cpu_play(board), computer)
            computer.win, running = win_check(board, computer)
            print_board(board)
            if running:
                running = not_full_board_check(board)
                
            if not computer.win and running:
                board, running = board_update(board, p1.option(), p1)
                p1.win, running = win_check(board, p1)
                if running:
                    running = not_full_board_check(board)
    
    if p1.win or computer.win:
        if p1.win:
            print_board(board)
            print(f"{p1.name} won!")
        else:
            print(f"Computer won!")
    else:
        print("Nobody won!")
            

def menu(board):
    print("TIC TAC TOE\n")
    print("'1' -> Player versus Computer")
    print("'2' -> Player versus Player")
    print("'3' -> Exit\n")

    while True:
        option = input(">> ")
        if option == "1":
            board = reset_board()
            player_vs_computer(board)
            break
        elif option == "2":
            board = reset_board()
            player_vs_player(board)
            break
        elif option == "3":
            exit()
        else:
            print("Invalid Input! Try again.")

def reset_board():
    board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "],
         ]

    return board
        

# Board Initial
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "],
         ]

# Game
option = ""

while True:
    menu(board)
    
    option = input("\nPlay again? [y/n]: ")
    if option == "y":
        option = ""
        board = reset_board()
        menu(board)
    elif option == "n":
        exit()
    else:
        print("Invalid Input! Try again.")







        
