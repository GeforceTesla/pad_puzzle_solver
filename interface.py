from operation import Operation
import random

if __name__ == "__main__":
    board = Operation()
    while 1:
        board.print_as_matrix(-1, -1)
        try:
            print 'Enter x Axis'
            x = int(raw_input())
        except ValueError:
            x = random.randint(0,5)
        try:
            print 'Enter y Axis'
            y = int(raw_input())
        except ValueError:
            y = random.randint(0,4)
        board.print_as_matrix(x, y)
        while 1:
            print 'Enter direction (up, down, left, write, ok, save, auto)'
            unitInput = raw_input()
            if unitInput == 'u':
                unitInput = 'up'
            elif unitInput == 'd':
                unitInput = 'down'
            elif unitInput == 'l':
                unitInput = 'left'
            elif unitInput == 'r':
                unitInput = 'right'
            elif unitInput == 'ok':
                board.release()
                board.print_as_matrix(x, y)
                break
            elif unitInput == 'save':
                board.release()
                board.print_as_matrix(x,y)
                board.write_file()
                break
            if unitInput != 'auto' and unitInput != 'a':
                x, y = board.swap_element(x, y, unitInput)
            else:
                print 'Enter auto search depth'
                depth = int(raw_input())
                x, y = board.solve_puzzle_full(x, y, depth)
            board.print_as_matrix(x, y)
            print 'current location: {0},{1}'.format(x,y)

