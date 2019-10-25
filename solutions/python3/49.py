class Solution:
    def groupAnagrams(self, strs):
        dic = collections.defaultdict(list)
        for s in strs: 
            dic["".join(sorted(s))].append(s)
        return list(dic.values())