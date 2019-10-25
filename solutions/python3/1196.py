class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        return bisect.bisect(list(itertools.accumulate(sorted(arr))), 5000)