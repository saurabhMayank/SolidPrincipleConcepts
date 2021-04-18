import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def test_board_has_nine_spots(self):
        board_obj = Board()
        self.assertEqual(len(board_obj.SPOTS), 9)
    
    def test_board_returns_first_row(self):
        board_obj = Board()
        row_one = ["0", "1", "2"]
        self.assertEqual(board_obj.first_row(), row_one)
    
    def test_board_returns_second_row(self):
        board_obj = Board()
        row_two = ["3", "4", "5"]
        self.assertEqual(board_obj.second_row(), row_two)
    
    def test_board_returns_third_row(self):
        board_obj = Board()
        row_three = ["6", "7", "8"]
        self.assertEqual(board_obj.third_row(), row_three)
    
    def test_print_board_to_console(self):
        board_obj = Board()
        self.assertEqual(board_obj.display(), "0|1|2\n3|4|5\n6|7|8")

if __name__ == '__main__':
    unittest.main()
