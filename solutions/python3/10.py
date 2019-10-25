class Solution:
    def isMatch(self, s, p):
        return bool(re.match(r"%s" %p, s)) and re.match(r"%s" %p, s).group(0) == s 