from collections import Counter as cnt
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return all(v == 1 for v in cnt(cnt(arr).values()).values())