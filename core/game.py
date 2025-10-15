class BackgammonGame:

    def __init__(self, player1, player2, board, dice):
        self.__player1__ = player1
        self.__player2__ = player2
        self.__board__ = board
        self.__dice__ = dice

    def get_player1(self):

        return self.__player1__

    def get_player2(self):

        return self.__player2__

    def get_board(self):

        return self.__board__

    def get_dice(self):

        return self.__dice__

    def start_game(self):

        self.__board__.reset_starting_position()
        self.__dice__.roll()
        return self.__dice__.get_last_roll()

    def restart_game(self):

        self.__board__.reset_board()
        self.__board__.reset_starting_position()
        self.__dice__.roll()
        return self.__dice__.get_last_roll()
