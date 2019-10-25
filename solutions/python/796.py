class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        return True if [A[i:]+A[:i] for i in range(len(A)) if A[i:]+A[:i]==B] else False