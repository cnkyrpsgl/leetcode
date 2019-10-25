class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = collections.Counter(s)
        res = ''
        for k, v in sorted(cnt.items(), key = lambda x: -cnt[x[0]]):
            res += k * v
        return res