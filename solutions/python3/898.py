class Solution:
    def subarrayBitwiseORs(self, A):
        nums, n, pre = set(), len(A), set()
        for a in A:
            pre = {a} | {num | a for num in pre}
            nums |= pre
        return len(nums)