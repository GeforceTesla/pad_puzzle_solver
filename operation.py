from matrix_op import MatrixOP
import random

class Operation(MatrixOP):

    def __init__(self):
        super(Operation, self).__init__()

    def solve_puzzle(self, init_x, init_y, path, matrixs):
        board = MatrixOP()
        x = init_x
        y = init_y
        board.set_matrix(matrixs)
        board.matrix = board.get_matrix()
        for i in path:
            x, y = board.swap_element(x, y, i)
        board.solver_release()
        return board.get_score()

    def createList(self, value):
        i = value
        path = []    
        path.append((i % 4) + 1)
        while i / 4 > 0: 
            i /= 4
            path.append((i % 4) + 1)
        return path

    def get_max_item(self):
        max_x = -1
        max_y = -1
        max_value = -1
        for x in range(6):
            for y in range(5):
                value = self.get_element(x, y)
                if value > max_value:
                    max_value = value
                    max_x = x
                    max_y = y
                    print max_value
        return max_x, max_y

    def solve_puzzle_full(self, ax=-1, ay=-1, depth=7):
        max_score = 0
        max_x = -1
        max_y = -1
        x = ax
        y = ay
        count = 4 ** depth
        if ax < 0 or ax > 5:
            x = random.randint(0,5)
        if ay < 0 or ay > 4:
            y = random.randint(0,4)
        for i in range(count):
            path = self.createList(i)
            scores = self.solve_puzzle(x, y, path, self.matrix)
            if scores > max_score:
                max_score = scores
                max_x = x
                max_y = y
                max_path = path
        try:
            max_path is None
        except UnboundLocalError:
                max_path = [1, 1, 3, 3, 1]
        print 'Max Score is: {0}'.format(max_score)
        print max_path
        for i in max_path:
            x, y = self.swap_element(x, y, i)
        return x, y
        

if __name__ == "__main__":
    boards = Operation()
    boards.print_as_matrix(-1, -1)
    boards.solve_puzzle_full()
    boards.print_as_matrix(-1, -1)

