class Solution:
    def getRow(self, rowIndex: int, row = [1]) -> List[int]:
        return self.getRow(rowIndex - 1, [a + b for a, b in zip([0] + row, row + [0])]) if rowIndex else row