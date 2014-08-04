from file_op import FileOP
import sys
import random

class MatrixOP(FileOP):

    def __init__(self):
        super(MatrixOP, self).__init__()
        self.matrix = self.get_matrix()
        self.clear_list = []
        self.clear_count = 0

    def print_as_matrix(self, x, y):
        print 'Current Board :'
        print '   0 1 2 3 4 5'
        print '   _ _ _ _ _ _'
        for i in range(self.row):
            sys.stdout.write('%d: '% i)
            for n in range(self.col):
                sys.stdout.write(str(self.matrix[self.col * i + n]))
                if i == y and x == n:
                    sys.stdout.write('<')
                else:
                    sys.stdout.write(' ')
            sys.stdout.write('\n')
        line = str(self.clear_count)
        line = 'score :' + line
        print line

    def get_score(self):
        return self.clear_count

    def get_element(self, ax, ay):
        return self.matrix[self.col * ay + ax]
   
    def set_element(self, ax, ay, value):
        self.matrix[self.col * ay + ax] = value

    def swap_element(self, ax, ay, direction):
        bx = ax
        by = ay
        if direction == 'up' or direction == 1:
            if ay > 0:
                by = ay - 1
        elif direction == 'down' or direction == 2:
            if ay < 4:
                by = ay + 1
        elif direction == 'left' or direction == 3:
            if ax > 0:
                bx = ax - 1
        elif direction == 'right' or direction == 4:
            if ax < 5:
                bx = ax + 1
        else:
            pass
        temp = self.get_element(bx, by)
        self.set_element(bx, by, self.get_element(ax, ay))
        self.set_element(ax, ay, temp)
        self.set_matrix(self.matrix)
        return bx, by

    def row_check(self):
        for i in range(self.row):
            count = 0
            current_element = self.get_element(0, i)
            #print '[row] current element is {0} and it is {1}'.format(current_element, current_element > 0)
            for n in range(self.col):
                if self.get_element(n, i) == current_element:
                    count += 1
                else:
                    count = 1
                    current_element = self.get_element(n, i)
                if count >= 3:
                    for k in range(count):
                        if current_element > 0:
                            if [n - k, i] not in self.clear_list:
                                self.clear_list.append([n - k, i])
            
    def col_check(self):
        for i in range(self.col):
            count = 0
            current_element = self.get_element(i, 0)
            #print '[col] current element is {0} and it is {1}'.format(current_element, current_element > 0)
            for n in range(self.row):
                if self.get_element(i, n) == current_element:
                    count += 1
                else:
                    count = 1
                    current_element = self.get_element(i, n)
                if count >= 3:
                    for k in range(count):
                        if current_element > 0:
                            if [i, n - k] not in self.clear_list:
                                self.clear_list.append([i, n - k])

    def clear_element(self):
        for i in self.clear_list:
            self.clear_count += 1
            self.set_element(i[0], i[1], 0)
        self.clear_list = []

    def solver_clear_element(self):
        for i in self.clear_list:
            self.clear_count += 1
            self.set_element(i[0], i[1], -1)
        self.clear_list = []

    def update_element(self):
        while 0 in self.matrix:
            for i in range(self.row):
                for n in range(self.col):
                    if i == 0:
                        if self.get_element(n, i) == 0:
                            self.set_element(n, i, random.randint(1,6))
                    else:
                        if self.get_element(n, i) == 0:
                            element = self.get_element(n, i - 1)
                            self.set_element(n, i, element)
                            self.set_element(n, i - 1, 0)

    def solver_update_element(self):
        while 0 in self.matrix:
            for i in range(self.row):
                for n in range(self.col):
                    if i == 0:
                        if self.get_element(n, i) == 0:
                            self.set_element(n, i, -1)
                    else:
                        if self.get_element(n, i) == 0:
                            element = self.get_element(n, i - 1)
                            self.set_element(n, i, element)
                            self.set_element(n, i - 1, 0)

    def release(self):
        self.row_check()
        self.col_check()
        while len(self.clear_list) != 0:
            self.clear_element()
            self.update_element()
            self.row_check()
            self.col_check()
        self.set_matrix(self.matrix)

    def solver_release(self):
        self.row_check()
        self.col_check()
        while len(self.clear_list) != 0:
            self.solver_clear_element()
            self.solver_update_element()
            self.row_check()
            self.col_check()
        self.set_matrix(self.matrix)

if __name__ == "__main__":
    new_matrix = MatrixOP()
    a = new_matrix.get_matrix()
    new_matrix.write_file()
    new_matrix.clear_element()
    new_matrix.update_element()
