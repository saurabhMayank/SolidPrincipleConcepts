class Board:
    """
    Class design depicts a bad code design of a System.
    Here the Employee Class will have many functionalities
    That means it will have many reasons to change.

    If the class has many reasons to change.
    Then that will make the class
    1. Rigid -> Because one modification will propel a lot of different
        modifications in order to avoid breakage of system.
        There will be lots of compilation errors, lots and lots of places
        the code will have to be changed.
    2. Fragile -> As the Codebase will increase, with lots and lots of
        rigid modules the code will depend on datastructures in
        undesirable ways between the modules which will cause run time
        errors and because of this modules will break in ways
        which can't be predicted.
    
    Class represents a tic tac toe board game.
    Responsibilities of the class :-
    1. Stores the value of spots on the board.
    2. Returns the board's rows.
    3. Prints the board out to the screen.
    """
    SPOTS = []

    def board(self):
        for index in range(0, 9):
            self.SPOTS.append(str(index))


    def first_row(self) -> list:
        first_row = []
        first_row.append(self.SPOTS[0])
        first_row.append(self.SPOTS[1])
        first_row.append(self.SPOTS[2])
        return first_row
    
    def second_row(self) -> list:
        second_row = []
        second_row.append(self.SPOTS[3])
        second_row.append(self.SPOTS[4])
        second_row.append(self.SPOTS[5])
        return second_row

    def third_row(self) -> list:
        third_row = []
        third_row.append(self.SPOTS[6])
        third_row.append(self.SPOTS[7])
        third_row.append(self.SPOTS[8])
        return third_row
    
    def display(self):
        formatted_first_row = self.SPOTS[0] + "|" + self.SPOTS[1] + "|"+ \
        self.SPOTS[2] + "\n" + self.SPOTS[3] + "|" + self.SPOTS[4]+ "|" + \
        self.SPOTS[5] + "\n" + self.SPOTS[6] + "|" + self.SPOTS[7] + "|" + \
        self.SPOTS[8]
        return formatted_first_row



board_obj = Board()
board_obj.board()
board_obj.first_row()
board_obj.second_row()
board_obj.third_row()
res = board_obj.display()
print(res)
