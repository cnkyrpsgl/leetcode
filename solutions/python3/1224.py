class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        def okay():
            if len(dic) == 1 and (1 in dic or 1 in dic.values()):
                return True 
            if len(dic) == 2:
                c1, c2 = sorted(dic.keys())
                if c2 - c1 == 1 and dic[c2] == 1 or (c1 == 1 and dic[1] == 1):
                    return True
        cnt = collections.Counter(nums)
        dic = collections.Counter(cnt.values())
        l = len(nums)
        for num in nums[::-1]:
            if okay():
                return l
            dic[cnt[num]] -= 1
            if not dic[cnt[num]]:
                dic.pop(cnt[num])
            cnt[num] -= 1
            if cnt[num]:
                dic[cnt[num]] += 1
            l -= 1
            if okay():
                return l