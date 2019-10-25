class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        m=len(grid[0])
        mx_i = [max(grid[i]) for i in range(n)]
        mx_j=[-float("inf")]*m
        for i in range(n): 
            for j in range(m): mx_j[j]=max(mx_j[j],grid[i][j])
        res=0
        for i in range(n):
            for j in range(m):
                prev=grid[i][j]
                grid[i][j]=min(mx_i[i],mx_j[j])
                res+=grid[i][j]-prev
        return res