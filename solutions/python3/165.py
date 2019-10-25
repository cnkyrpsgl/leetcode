class Solution:
    def compareVersion(self, version1, version2):
        def getNum(s):
            if not s: return (None, None)
            for i in range(len(s)):
                if s[i] == ".": return (s[i + 1:], int(s[:i]))
            return (None, int(s))
        while True:
            version1, n1 = getNum(version1)
            version2, n2 = getNum(version2)
            if version1 == version2 == n1 == n2 == None: return 0
            if n1 != None and n1 > 0 and (n2 == None or n1 > n2): return 1
            if n2 != None and n2 > 0 and (n1 == None or n2 > n1): return -1