class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        for row in matrix:
            for col in range(1, len(row)):
                row[col] += row[col-1]
        self.matrix = matrix
        

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        original = self.matrix[row][col]
        if col != 0:
            original -= self.matrix[row][col-1]
            
        diff = original - val
        
        for y in range(col, len(self.matrix[0])):
            self.matrix[row][y] -= diff

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum = 0
        for x in range(row1, row2+1):
            sum += self.matrix[x][col2]
            if col1 != 0:
                sum -= self.matrix[x][col1-1]
        return sum