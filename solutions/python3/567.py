class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2): return False
        dic = collections.defaultdict(int)
        for i in range(len(s1)):
            dic[s1[i]] += 1
            if dic[s1[i]] == 0: del dic[s1[i]]
            dic[s2[i]] -= 1
            if dic[s2[i]] == 0: del dic[s2[i]]
        i = 0
        for j in range(len(s1), len(s2)):
            if not dic: return True
            dic[s2[j]] -= 1
            if dic[s2[j]] == 0: del dic[s2[j]]
            dic[s2[i]] += 1
            if dic[s2[i]] == 0: del dic[s2[i]]
            i += 1
        return not dic