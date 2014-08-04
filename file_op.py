import sys
import random

class FileOP(object):

    file_real = 'record.txt'

    def __init__(self):
        self.read_file()
        self.matrix_create()

    def read_file(self):
        try:
            self.file = open(self.file_real, 'r+')
        except IOError:
            self.file = open(self.file_real, 'w')
            self.file = open(self.file_real, 'r+')
        self.data = self.file.read()
        self.file.close()
        self.row = 5
        self.col = 6

    def get_matrix(self):
        return map(int, list(self.data[0:self.row * self.col]))

    def set_matrix(self, inputs):
        self.data = map(str, list(inputs))

    def matrix_create(self):
        array = []
        if self.data == '':
            for i in range(self.row * self.col):
                array.append(random.randint(1,6))
            self.data = array

    def write_file(self):
        self.file = open(self.file_real, 'w')
        for i in self.data:
            self.file.write(str(i))
        self.file.close()

if __name__ == "__main__":
    new_file = FileOP()
    print new_file.get_matrix()
    new_file.write_file()
