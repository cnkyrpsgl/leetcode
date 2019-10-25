class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        glasses=[[poured if i==0 and j==0 else 0 for i in range(j+1)] for j in range(query_row+1)]
        for i in range(1,len(glasses)):
            for j in range(len(glasses[i])):
                if j-1>=0 and glasses[i-1][j-1]>1: glasses[i][j]+=(glasses[i-1][j-1]-1)/2
                if j<=i-1 and glasses[i-1][j]>1: glasses[i][j]+=(glasses[i-1][j]-1)/2
        return glasses[query_row][query_glass] if glasses[query_row][query_glass]<=1 else 1