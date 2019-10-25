class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            for i in range(1, n):
                row[i] += row[i-1]
                
        res = 0
        for i in range(n):
            for j in range(i, n):
                c = {0:1}
                cur = 0
                for row in matrix:
                    cur += row[j] - (row[i-1] if i else 0)
                    
                    if cur - target in c:
                        res += c[cur-target]
                    
                    c[cur] = c.get(cur, 0) + 1
        return res