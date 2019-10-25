class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic, pair = {}, 0
        for num in nums:
            if (num-k in dic or num+k in dic) and (not num in dic or (k==0 and dic[num]==1)) and k>=0: 
                if num-k in dic and k!=0: pair+=1
                if num+k in dic: pair+=1 
                if num in dic: dic[num]+=1; continue
            if num in dic: continue
            dic[num]=1
        return pair