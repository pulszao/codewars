import math


class Sudoku(object):
    def __init__(self, data):
        self.data = data
        self.N = len(data)
        self.block_N = int(math.sqrt(self.N))

    def validade_row(self, row):
        size = len(row)
        # Validade row
        while size > 0:
            if size not in row:
                return False
            size -= 1
        return True

    def is_valid(self):
        valid_input = (
            isinstance(self.data, list) and
            all(isinstance(row, list) and all(type(item) == int for item in row) for row in self.data)
        )
        if float(self.N) != int(self.N) or not valid_input:
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
        for i in range(self.block_N):
            for j in range(self.block_N):
                block = []
                for x in range(i * self.block_N, (i + 1) * self.block_N):
                    for y in range(j * self.block_N, (j + 1) * self.block_N):
                        block.append(self.data[x][y])
                if not self.validade_row(block):
                    return False

        return True