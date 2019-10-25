class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        t = set(T)
        t2 = set(S)
        from collections import Counter as ct
        c = ct(T)
        s = [char * c[char] for char in S if char in t]
        add = [char * c[char] for char in t - t2]
        return "".join(s + add)