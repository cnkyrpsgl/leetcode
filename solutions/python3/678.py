class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, left_star = [], []
        for i in range(len(s)):
            if s[i] == "(": left.append([s[i], i])
            elif s[i] == "*": left_star.append([s[i], i])
            elif left and left[-1][0] == "(": left.pop()
            elif left_star: left_star.pop()
            else: return False
        while left and left_star and left[-1][1]< left_star[-1][1]: left.pop(); left_star.pop()
        return not left   