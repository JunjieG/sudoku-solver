from copy import deepcopy


class Sudoku:
    def __init__(self, filename: str = ""):
        self._starting_board = []
        self._solution = []
        if filename:
            self.create_board(filename)
        
    def create_board(self, filename: str):
        with open(filename, 'r') as board_file:
            for line in board_file:
                line = line.strip('\n')
                if len(line.split('|')) != 9: raise ValueError('A row must have 9 elements')
                row = [int(element.strip('\n')) if element and element != ' ' else 0 for element in line.split('|')]
                self._starting_board.append(row)
        self._solution = deepcopy(self._starting_board)
    
    def solve_game(self):
        if not self._starting_board:
            print('Please create a starting board first using the create_board() function')
            return
        self._solve_game_recur()
    
    def _solve_game_recur(self):
        for row_num, row in enumerate(self._solution):
            for col_num, element in enumerate(row):
                if element == 0:
                    for possible_value in range(10):
                        if self._is_valid(possible_value, row_num, col_num):
                            self._solution[row_num][col_num] = possible_value
                            if self._solve_game_recur():
                                return True
                            self._solution[row_num][col_num] = 0
                    return False
        return True

    
    def _check_exists_column(self, value, col_num):
        for row in self._solution:
            if row[col_num] == value:
                return True
        return False

    def _check_exists_row(self, value, row_num):
        for element in self._solution[row_num]:
            if element == value:
                return True
        return False
    
    def _check_exists_box(self, value, box_range):
        for row_num in range(box_range[0], box_range[0] + 3):
            for col_num in range(box_range[1], box_range[1] + 3):
                if self._solution[row_num][col_num] == value:
                    return True
        return False
    
    def _is_valid(self, possible_value, row_num, col_num):
        exists_in_column = self._check_exists_column(possible_value, col_num)
        exists_in_row = self._check_exists_row(possible_value, row_num)
        exists_in_box = self._check_exists_box(possible_value, self._get_box_range_for_value(row_num, col_num))
        if not exists_in_row and not exists_in_column and not exists_in_box:
            return True
        return False
                
    def _get_box_range_for_value(self, row_num, col_num):
        """Given the row number and the column number of an element, return the row and column start index for that box

        Args:
            row_num (int): Row number of the element.
            col_num (int): Column number of the element.

        Returns:
            tuple: Tuple of two elements, first being the row start index and second being the column start index.
        """
        row_start = 0
        col_start = 0
        if row_num > 2 and row_num <= 5:
            row_start = 3
        elif row_num > 5:
            row_start = 6
        if col_num > 2 and col_num <= 5:
            col_start = 3
        elif col_num > 5:
            col_start = 6
        return (row_start, col_start)
            
    
    def __str__(self):
        result = ""
        for row_num, row in enumerate(self._starting_board):
            for col_num, element in enumerate(row):
                if element:
                    result = result + str(element) + " "
                else:
                    result = result + "  "
                if col_num == 2 or col_num == 5:
                    result += "|"
                elif col_num == 8:
                    result += '\n'
            if row_num == 2 or row_num == 5:
                result += "------+------+------\n"

        result += "\nSolution:\n"
        for row_num, row in enumerate(self._solution):
            for col_num, element in enumerate(row):
                if element:
                    result = result + str(element) + " "
                else:
                    result = result + "  "
                if col_num == 2 or col_num == 5:
                    result += "|"
                elif col_num == 8:
                    result += '\n'
            if row_num == 2 or row_num == 5:
                result += "------+------+------\n"
        return result