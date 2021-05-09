class BoardShaper:
    """
     Responsibility of Board Shaper:
     1. How the steps are being manipulated per the rules of
     Tic tac toe.
    """

    SIZE_OF_BOARD = 0

    def board_shaper(self, size: int):
        self.SIZE_OF_BOARD = size

    def row_indexes(self) -> list:
        row_indexes = []
        for index in range(0, self.SIZE_OF_BOARD):
            row = []
            for inner_index in range(0, self.SIZE_OF_BOARD):
                row.append((index * self.SIZE_OF_BOARD) + inner_index)
            row_indexes(row)
        return row_indexes
    
