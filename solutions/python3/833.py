class Solution:
    def findReplaceString(self, s, indexes, sources, targets):
        res, dic, j = "", {}, 0
        for i in range(len(sources)):
            if s.find(sources[i], indexes[i]) == indexes[i]: dic[indexes[i]] = (sources[i], targets[i])
        while j < len(s):
            res += j in dic and dic[j][1] or s[j]
            j += j in dic and len(dic[j][0]) or 1
        return res