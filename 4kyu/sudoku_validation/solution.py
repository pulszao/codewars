import math


class Sudoku(object):
    def __init__(self, data):
        self.data = data
        self.N = math.sqrt(len(data[0]))
        self.block_N = int(len(data[0]) / self.N)

    def validade_row(self, row):
        size = len(row)
        # Validade row
        while size > 0:
            if size not in row:
                return False
            size -= 1
        return True

    def is_valid(self):
        if self.N % 2 > 0:
            return False

        # Validate row
        for row in self.data:
            if not self.validade_row(row):
                return False

        # Validate column
        transposed = [list(row) for row in zip(*self.data)]
        for row in transposed:
            if not self.validade_row(row):
                return False

        # Validate block
        for row_index, row in enumerate(self.data):
            for element in row:
                x = row.index(element) // self.block_N
                y = row_index // self.block_N

        return True


if __name__ == '__main__':
    badSudoku2 = Sudoku([
        [1, 4, 2, 3],
        [3, 2, 4, 1],
        [4, 1, 3, 2],
        [2, 3, 1, 4]
    ])

    print(badSudoku2.is_valid())
