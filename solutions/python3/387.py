class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = collections.defaultdict(int)
        for c in s:
            dic[c] += 1
        for i, c in enumerate(s):
            if dic[c] == 1: return i
        return -1