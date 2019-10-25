class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        start = distinct = 0
        cnt = collections.defaultdict(int)
        for c in s:
            cnt[c] += 1
            if cnt[c] == 1:
                distinct += 1
            if distinct > 2:
                cnt[s[start]] -= 1
                if not cnt[s[start]]:
                    distinct -= 1
                start += 1
        return len(s) - start