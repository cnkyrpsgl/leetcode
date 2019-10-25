class Solution:
    def maxLength(self, arr: List[str]) -> int:
        bfs = [""]
        for b in filter(lambda x: len(x) == len(set(x)), arr):
            bfs += [a + b for a in bfs if not set(a) & set(b)]
        return max(map(len, bfs))
