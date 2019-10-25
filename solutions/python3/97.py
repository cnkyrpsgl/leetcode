class Solution:
    def isInterleave(self, s1, s2, s3):
        def dfs(i, j, k):
            if (i, j, k) not in memo:
                memo[(i, j, k)] = k>=l3 or (i<l1 and s3[k]==s1[i] and dfs(i+1,j,k+1)) or (j<l2 and s3[k]==s2[j] and dfs(i,j+1,k+1))
            return memo[(i, j, k)]
        l1, l2, l3, memo = len(s1), len(s2), len(s3), {}
        if l3 != l1 + l2: return False
        return dfs(0, 0, 0)