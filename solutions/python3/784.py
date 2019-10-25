class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        bfs = ['']
        for c in S:
            if c.isdigit():
                bfs = [s + c for s in bfs]
            else:
                bfs = [s + c.lower() for s in bfs] + [s + c.upper() for s in bfs]
        return bfs