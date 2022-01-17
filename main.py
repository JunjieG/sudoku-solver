from sudoku import Sudoku

def main():
    sudoku = Sudoku()
    sudoku.create_board("sudoku.txt")
    print(sudoku)

if __name__ == '__main__':
    main()