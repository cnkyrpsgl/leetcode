class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        bfs = [[]]
        for num in range(1, n + 1):
            bfs += [arr + [num] for arr in bfs if len(arr) < k]
        return [arr for arr in bfs if len(arr) == k]