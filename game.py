import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class Menu:
    def main_menu(self):
        text = '''
        Welcome to Tic-Tac-Toe! 
        1. Start game 
        2. Quit game 
        '''
        while True:
            choice = input(text).strip()
            if choice in ['1', '2']:
                return choice
            else:
                print("Invalid input. Please enter 1 or 2.")

    def end_menu(self):
        text = '''
        Game over.
        1. Restart game
        2. Quit game
        '''
        while True:
            choice = input(text).strip()
            if choice in ['1', '2']:
                return choice
            else:
                print("Invalid input. Please enter 1 or 2.")

class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i + 3]))
            if i < 6:
                print("-" * 5)

    def is_valid_move(self, choice):
        return self.board[choice - 1].isdigit()

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]

class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name (letters only): ").strip()
            if name.isalpha():
                self.name = name
                break
            print("Invalid name. Please use letters only.")

    def choose_symbol(self, existing_symbols):
        while True:
            symbol = input(f"{self.name}, enter your symbol (one letter): ").strip()
            if symbol.isalpha() and len(symbol) == 1 and symbol not in existing_symbols:
                self.symbol = symbol
                break
            if symbol in existing_symbols:
                print("Symbol already taken. Please choose a different symbol.")
            else:
                print("Invalid symbol. Please enter a single letter.")

class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        print("Welcome to Tic-Tac-Toe!")
        choice = self.menu.main_menu()
        if choice == "1":
            self.setup_players()
            clear_screen()
            self.board.display_board()
            self.playing()
        else:
            self.quit_game()

    def setup_players(self):
        symbols = []
        for number, player in enumerate(self.players, start=1):
            print(f"Player {number}, enter your details")
            player.choose_name()
            player.choose_symbol(symbols)
            symbols.append(player.symbol)
            clear_screen()

    def quit_game(self):
        print("Thanks for playing!")
        exit()  # Ensure the program exits

    def playing(self):
        while True:
            self.play_turn()
            if self.check_win():
                clear_screen()
                self.board.display_board()
                print(f"{self.players[1 - self.current_player_index].name} wins!")
                choice = self.menu.end_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
            elif self.check_draw():
                clear_screen()
                self.board.display_board()
                print("It's a draw!")
                choice = self.menu.end_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()

    def restart_game(self):
        self.board.reset_board()
        clear_screen()
        self.current_player_index = 0
        self.board.display_board()
        self.playing()

    def check_win(self):
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for pattern in win_patterns:
            if self.board.board[pattern[0]] == self.board.board[pattern[1]] == self.board.board[pattern[2]]:
                return True
        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    def play_turn(self):
        current_player = self.players[self.current_player_index]
        while True:
            try:
                cell_choice = int(input(f"{current_player.name}'s turn ({current_player.symbol}): Choose a cell between 1 and 9: ").strip())
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, current_player.symbol):
                    clear_screen()
                    self.board.display_board()
                    break
                else:
                    print("Invalid choice. Please choose an empty cell between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
        self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

if __name__ == "__main__":
    game = Game()
    game.start_game()

