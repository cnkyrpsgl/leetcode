class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s): return s
        row, direction, res = 0, -1, [""] * numRows
        for char in s:
            res[row] += char
            if row == 0 or row == numRows - 1: direction *= -1 
            row += direction
        return "".join(res) 