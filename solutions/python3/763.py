class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        sizes = []
        while S:
            i = 1
            while set(S[:i]) & set(S[i:]):
                i += 1
            sizes.append(i)
            S = S[i:]
        return sizes