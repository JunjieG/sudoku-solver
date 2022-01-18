from sudoku import Sudoku

def main():
    sudoku = Sudoku()
    sudoku.create_board("sudoku.txt")
    sudoku.solve_game()
    print(sudoku)

if __name__ == '__main__':
    main()