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
        self._solution = self._starting_board
    
    
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
        return result