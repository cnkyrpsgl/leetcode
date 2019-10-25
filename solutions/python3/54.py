class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        seen = set()
        def dfs(i, j, d):
            seen.add((i, j))
            res.append(matrix[i][j])
            if d == 'r':
                if j + 1 < n and (i, j + 1) not in seen:
                    dfs(i, j + 1, d)
                elif i + 1 < m and (i + 1, j) not in seen:
                    dfs(i + 1, j , 'd')
            elif d == 'd':
                if i + 1 < m and (i + 1, j) not in seen:
                    dfs(i + 1, j , d)
                elif j and (i, j - 1) not in seen:
                    dfs(i, j - 1, 'l')
            elif d == 'l':
                if j and (i, j - 1) not in seen:
                    dfs(i, j - 1, d)
                elif i and (i - 1, j) not in seen:
                    dfs(i - 1, j, 'u')
            else:
                if i and (i - 1, j) not in seen:
                    dfs(i - 1, j, d)
                elif j + 1 < n and (i, j + 1) not in seen:
                    dfs(i, j + 1, 'r')
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        dfs(0, 0, 'r')
        return res
        