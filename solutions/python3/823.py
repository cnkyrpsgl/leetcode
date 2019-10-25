class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        nums, res, trees, factors = set(A), 0, {}, collections.defaultdict(set)
        for i, num in enumerate(A):
            for n in A[:i]:
                if num % n == 0 and num // n in nums: factors[num].add(n)
        for root in A:
            trees[root] = 1
            for fac in factors[root]: trees[root] += trees[fac] * trees[root // fac]
        return sum(trees.values()) % ((10 ** 9) + 7)