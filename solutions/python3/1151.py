class Solution:
    def minSwaps(self, data: List[int]) -> int:
        l = data.count(1)
        mn = cur = data[:l].count(0)
        for i in range(l, len(data)):
            cur += not data[i] 
            cur -= not data[i - l]
            mn = min(mn, cur)
        return mn
        