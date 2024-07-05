class TicTacToe:
    def __init__(self):
        # Initialize the board with empty spaces and set the starting player
        self.board = {
            '1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '
        }
        self.current_player = '1'  # Start with Player 1
        self.player_symbols = {'1': 'X', '2': 'O'}  # Default symbols for players

    def display_board(self):
        # Display the current state of the game board
        print(f"{self.board['1']} | {self.board['2']} | {self.board['3']}")
        print('--+---+--')
        print(f"{self.board['4']} | {self.board['5']} | {self.board['6']}")
        print('--+---+--')
        print(f"{self.board['7']} | {self.board['8']} | {self.board['9']}")

    def display_instructions(self):
        # Display the instructions for the game, including board positions
        print("Welcome to Tic-Tac-Toe Game!")
        print("Here's the numbering for the board positions:")
        print(" 1 | 2 | 3 ")
        print(" --+---+-- ")
        print(" 4 | 5 | 6 ")
        print(" --+---+-- ")
        print(" 7 | 8 | 9 ")
        print("Players will take turns to place their mark (X or O) on the board.")

    def choose_symbols(self):
        # Allow Player 1 to choose their symbol (X or O)
        while True:
            choice = input("Player 1, please choose your symbol (X or O): ").upper()
            if choice in ['X', 'O']:
                self.player_symbols['1'] = choice
                self.player_symbols['2'] = 'O' if choice == 'X' else 'X'
                print(f"Player 1 is {self.player_symbols['1']}, Player 2 is {self.player_symbols['2']}.")
                break
            else:
                print("Invalid choice! Please choose 'X' or 'O'.")

    def make_move(self, position):
        # Update the board with the current player's symbol if the position is valid
        symbol = self.player_symbols[self.current_player]
        if self.board[position] == ' ':
            self.board[position] = symbol
            return True
        else:
            print("Invalid move! Position already taken.")
            return False

    def check_winner(self):
        # Check if there's a winner by examining all possible winning combinations
        winning_combinations = [
            ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],  # horizontal
            ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],  # vertical
            ['1', '5', '9'], ['3', '5', '7']                    # diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        return None

    def check_tie(self):
        # Check if the game is a tie (no empty spaces left)
        for key in self.board:
            if self.board[key] == ' ':
                return False
        return True

    def switch_player(self):
        # Switch to the other player
        self.current_player = '2' if self.current_player == '1' else '1'

    def play_game(self):
        # Main game loop: display instructions, choose symbols, and alternate moves until there's a winner or a tie
        self.display_instructions()
        self.choose_symbols()
        while True:
            self.display_board()
            move = input(f"Player {self.current_player}, please enter your move (1-9): ")
            if move not in self.board:
                print("Invalid input! Please enter a number between 1 and 9.")
                continue
            if self.make_move(move):
                winner = self.check_winner()
                if winner:
                    self.display_board()
                    winning_player = '1' if winner == self.player_symbols['1'] else '2'
                    print(f"Congratulations! Player {winning_player} wins!")
                    break
                if self.check_tie():
                    self.display_board()
                    print("The game is a tie!")
                    break
                self.switch_player()
