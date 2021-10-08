from typing import List

class Matrix(object):
    def __init__(self, matrix_string: str) -> None:
        self.matrix = [
            [int(cell) for cell in row.split()] for row in matrix_string.splitlines()
        ]
        self._columns = [
            [row[index] for row in self.matrix] for index in range(len(self.matrix[0]))
        ]
    def row(self, index: int) -> List[int]:
        return self.matrix[index - 1]
    def column(self, index: int) -> List[int]:
        return self._columns[index - 1]