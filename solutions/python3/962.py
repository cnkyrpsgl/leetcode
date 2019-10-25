class Solution:
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ind, mx, index = float("inf"), 0, collections.defaultdict(list)
        for i, num in enumerate(A):
            index[num].append(i)
        A.sort()
        for i in range(len(A)):
            mx = max(mx, index[A[i]][-1] - ind)
            ind = min(ind, index[A[i]][0])
        return mx