from board import Board


class BoardPresenter:
    """
        Display the results of the tic tac toe board
    """

    BOARD_OBJ = Board()


    def board_presenter(self, board: Board):
        self.BOARD_OBJ = board
    
    def display_board(self):
        formatted_board = ""
        n = self.BOARD_OBJ.SIZE_OF_BOARD
        for index in range(0, n * n):
            border_or_newline = ""
            if((index + 1) % n):
                border_or_newline = border_or_newline + "\n"
            else:
                border_or_newline = border_or_newline + "|"
            formatted_board = formatted_board + self.BOARD_OBJ.SPOTS[i]
            formatted_board = formatted_board + border_or_newline
        
        return formatted_board

