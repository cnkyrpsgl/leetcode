class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int, cnt: int = 0) -> int:
        odds = [-1] + [i for i, num in enumerate(nums) if num % 2] + [len(nums)]
        return sum(
            (odds[j - k + 1] - odds[j - k]) * (odds[j + 1] - odds[j])
            for j in range(k, len(odds) - 1)
        )

