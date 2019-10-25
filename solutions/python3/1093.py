class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        arr = [(i, c * 1.0) for i, c in enumerate(count) if c]
        acc = list(itertools.accumulate(count, lambda x, y: x + y))
        mean = sum(i * c for i, c in arr) / acc[-1] 
        mode = max(arr, key = lambda x: x[1])[0] * 1.0
        m1 = bisect.bisect(acc, (acc[-1] - 1) // 2)
        m2 = bisect.bisect(acc, acc[-1] // 2)
        return [arr[0][0] * 1.0, arr[-1][0] * 1.0, mean, (m1 + m2) / 2.0, mode]
        