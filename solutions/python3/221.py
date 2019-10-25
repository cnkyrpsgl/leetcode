class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res, count = 0, 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] != 0:
                    count = 1
                    if j>0 and int(matrix[i][j-1]) != 0: matrix[i][j] += int(matrix[i][j-1])
                    if i-1>=0 and int(matrix[i-1][j]) != 0:
                        k, curr = i-1, []
                        while k>=0 and k>=i-matrix[i][j]+1 and int(matrix[k][j]) != 0:
                            if matrix[k][j]>= count+1:
                                curr.append(matrix[k][j])
                                if min(curr)>= count+1: count += 1
                            else: break
                            k -= 1
                res = max(res, count**2)
        return res