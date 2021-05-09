class Board:
    """
      Good example of Board class

      Responsibilities of Board Class
      1. Knowing the values of its spots.
    """
    SIZE_OF_BOARD = 0
    SPOTS = []

    def Board(self, size: int):
        self.SIZE_OF_BOARD = size
        for index in range(0, size):
            self.SPOTS.append(str(3 * index))
            self.SPOTS.append(str(3 * index + 1))
            self.SPOTS.append(str(3 * index + 2))
    

    
    def values_at(self, indexes: list) -> list:
        values = []
        for index in indexes:
            values.append(index)
        
        return values
