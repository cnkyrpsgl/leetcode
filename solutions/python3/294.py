class Solution:
    def canWin(self, s):
        choices = {i for i in range(1, len(s)) if s[i] == s[i - 1] == "+"} 
        def dfs(arr, moves, turn):
            if not moves:
                return turn == 1
            elif turn:
                return all(dfs(arr + [m], moves - {m - 1, m, m + 1}, 1 - turn) for m in moves) 
            else:
                return any(dfs(arr + [m], moves - {m - 1, m, m + 1}, 1 - turn) for m in moves) 
        return not dfs([], choices, 1)     