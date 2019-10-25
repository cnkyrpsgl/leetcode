class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return collections.Counter(A).most_common(1)[0][0]