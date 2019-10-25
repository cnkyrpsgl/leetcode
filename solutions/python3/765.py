class Solution:
    def minSwapsCouples(self, row):
        res, index = 0, {num: i for i, num in enumerate(row)}
        for i in range(0, len(row), 2):
            if row[i] % 2 == 0 and row[i + 1] != row[i] + 1: 
                f = row[i + 1]
                row[i + 1], row[index[row[i] + 1]] = row[i] + 1, row[i + 1]
                index[row[i] + 1], index[f] = i + 1, index[row[i] + 1]
                res += 1
            elif row[i] % 2 != 0 and row[i + 1] != row[i] - 1:
                f = row[i + 1]
                row[i + 1], row[index[row[i] - 1]], index[row[i + 1]] = row[i] - 1, row[i + 1], index[row[i] - 1]
                index[row[i] - 1], index[f] = i + 1, index[row[i] - 1]
                res += 1
        return res