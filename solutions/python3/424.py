class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dic, start, end = {}, 0, 0
        for end in range(1, len(s)+1):
            if not s[end-1] in dic: dic[s[end-1]] = 1
            else: dic[s[end-1]] += 1
            if end-start-max(dic.values()) > k: 
                dic[s[start]] -= 1
                start += 1
        return end-start